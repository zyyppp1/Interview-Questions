const https = require("https");

// ✅ immediately use API_KEY_DO_NOT_MODIFY
const OPENAI_API_KEY = "API_KEY_DO_NOT_MODIFY";

const OPENAI_API_ENDPOINT = "api.openai.com";
const OPENAI_API_PATH = "/v1/chat/completions";

const fetchChatCompletion = (messages, callback) => {
    const postData = JSON.stringify({
        model: "gpt-4-0613",  // ✅ make sure choose the right model
        messages: messages,
        max_tokens: 150,
        temperature: 0.1
    });

    const options = {
        hostname: OPENAI_API_ENDPOINT,
        path: OPENAI_API_PATH,
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer API_KEY_DO_NOT_MODIFY"
        }
    };

    const req = https.request(options, (res) => {
        let responseData = "";

        res.on("data", (chunk) => {
            responseData += chunk;
        });

        res.on("end", () => {
            try {
                const responseJSON = JSON.parse(responseData);
                console.log("✅ API Response:", JSON.stringify(responseJSON, null, 2));
                callback(null, responseJSON);  // ✅ return api response
            } catch (error) {
                callback(error, null);
            }
        });
    });

    req.on("error", (error) => {
        callback(error, null);
    });

    req.write(postData);
    req.end();
};

// **main function**
const main = () => {
    const messages = [
        { role: "system", content: "You are a helpful assistant." },
        { role: "user", content: "Define 'evaporation'." }
    ];

    fetchChatCompletion(messages, (error, response) => {
        if (error) {
            console.error("Error fetching completion:", error);
            return;
        }
        console.log(JSON.stringify(response, null, 2)); // ✅ output full json
    });
};

// run main
main();
