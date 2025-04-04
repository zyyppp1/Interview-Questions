import requests
from datetime import datetime, timedelta
from collections import defaultdict

USER_KEY = "c01b75d56ae6ce15f2309cc7b9f1"
TEST_DATA_URL = f"https://candidate.hubteam.com/candidateTest/v3/problem/test-dataset?userKey={USER_KEY}"
TEST_RESULT_URL = f"https://candidate.hubteam.com/candidateTest/v3/problem/test-result?userKey={USER_KEY}"
REAL_DATA_URL = f"https://candidate.hubteam.com/candidateTest/v3/problem/dataset?userKey={USER_KEY}"
REAL_RESULT_URL = f"https://candidate.hubteam.com/candidateTest/v3/problem/result?userKey={USER_KEY}"

def timestamp_to_utc_date(ts):
    return datetime.fromtimestamp(ts / 1000).strftime('%Y-%m-%d')

def fetch_test_data(url):
    response = requests.get(url)
    print("Fatch Function, API Response:", response.status_code)
    return response.json()['callRecords']

def post_test_result(url,results):
    return requests.post(url, json={"results": results})

def split_calls_by_day(calls):
    result = defaultdict(list)
    for call in calls:
        cid = call['customerId']
        call_id = call['callId']
        start = call['startTimestamp']
        end = call['endTimestamp']
    # focus on the day, and ignore the time by replace.
        start_dt = datetime.fromtimestamp(start / 1000).replace(hour=0, minute=0, second=0, microsecond=0)
        end_dt = datetime.fromtimestamp(end / 1000).replace(hour=0, minute=0, second=0, microsecond=0)
    # Calculate the number of days between start and end
        num_days = (end_dt - start_dt).days + 1

        for i in range(num_days):
    # Calculate the start and end timestamps for each day
            day_start = int((start_dt + timedelta(days=i)).timestamp() * 1000)
            day_end = int((start_dt + timedelta(days=i + 1)).timestamp() * 1000)
    
            part_start = max(start, day_start)
            part_end = min(end, day_end)
            if part_start < part_end:
                date = timestamp_to_utc_date(part_start)
                result[(cid, date)].append({
                    "callId": call_id,
                    "start": part_start,
                    "end": part_end
                })
    return result

def calculate_max_concurrency(calls_by_customer_date):
    results = []
    # Iterate through each customer and date    
    for (cid, date), call_list in calls_by_customer_date.items():
        events = []
    
        for call in call_list:
            events.append((call['start'], 'start', call['callId']))
            events.append((call['end'], 'end', call['callId']))

        events.sort()
        current = set()
        max_count = 0
        max_timestamp = 0
        max_call_ids = []
    # Iterate through the events to find the maximum concurrency
        for ts, typ, call_id in events:
            if typ == 'start':
                current.add(call_id)
                if len(current) > max_count:
                    max_count = len(current)
                    max_timestamp = ts
                    max_call_ids = list(current)
            else:
                current.discard(call_id)
    
        results.append({
            "customerId": cid,
            "date": date,
            "maxConcurrentCalls": max_count,
            "timestamp": max_timestamp,
            "callIds": max_call_ids
        })
    return results

if __name__ == "__main__":
    # get the call data
    testcalls = fetch_test_data(TEST_DATA_URL)
    # split calls by day
    testcalls_calls_by_day = split_calls_by_day(testcalls)
    # calculate max concurrency
    test_result_data = calculate_max_concurrency(testcalls_calls_by_day)
    # post the result
    test_response = post_test_result(TEST_RESULT_URL,test_result_data)

    print("Status Code:", test_response.status_code)
    print("Response:", test_response.text)