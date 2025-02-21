import random

class FruitGame:
    def __init__(self, num_players):
        self.fruits = {"Apple": 10, "Banana": 10, "Cherry": 10, "Grape": 10}  #set fruits
        self.raven_position = 0  # raven position init
        self.max_raven_steps = 9  # raven's end
        self.players = [f"Player {i+1}" for i in range(num_players)]
        self.dice_faces = [1, 2, 3, 4, 5, 6]  # dice set
        self.current_player_index = 0  # user index

    def roll_dice(self):
        # use random to roll dice
        return random.choice(self.dice_faces)

    def remove_fruit(self, fruit):
        if self.fruits[fruit] > 0:
            self.fruits[fruit] -= 1
            print(f"{self.players[self.current_player_index]} removed one {fruit}. Remaining: {self.fruits[fruit]}")
        else:
            print(f"{self.players[self.current_player_index]} failed to remove {fruit}. 2no one left")

    def remove_two_random_fruits(self):
        #find the left fruits , which is available for remove.
        available_fruits = [fruit for fruit, count in self.fruits.items() if count > 0]
        if len(available_fruits) >= 2:
            # use chosen_fruit to save the result for random.
            chosen_fruits = random.sample(available_fruits, 2)
        elif len(available_fruits) == 1:
            # if only one kind of fruit left,choose it twice.
            chosen_fruits = [available_fruits[0], available_fruits[0]]  
        else:
            return  # no available fruit
        # delete chosing fruit
        for fruit in chosen_fruits:
            self.remove_fruit(fruit)

    def move_raven(self):
        print(f"{self.players[self.current_player_index]} roll a dice for 6 ")
        self.raven_position += 1
        print(f"Raven moves forward! Position: {self.raven_position}/{self.max_raven_steps}")

    def check_game_over(self):
        if all(count == 0 for count in self.fruits.values()):
            print("\nAll fruits have been taken! Players win! 🎉")
            return True
        if self.raven_position == self.max_raven_steps:
            print("\nRaven reached the end! Raven wins! 🦅")
            return True
        return False

    def play_game(self):
        print("\n🍎🍌🍒🍇 Welcome to the Raven-Fruit Game! 🍎🍌🍒🍇\n")
        while True:
            player = self.players[self.current_player_index]

            dice_result = self.roll_dice()


            if 1 <= dice_result <= 4:
                fruit_name = list(self.fruits.keys())[dice_result - 1]
                self.remove_fruit(fruit_name)
            elif dice_result == 5:
                self.remove_two_random_fruits()
            elif dice_result == 6:
                self.move_raven()
            #after operation of this round , check if the game ends.
            if self.check_game_over():
                break

            # move to next player
            self.current_player_index = (self.current_player_index + 1) % len(self.players)

# 运行游戏
num_players = int(input("Enter number of players: "))
game = FruitGame(num_players)
game.play_game()