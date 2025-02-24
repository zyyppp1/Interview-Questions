import random
#  import random for basket operation.

class FruitGame:# Yeah , maybe I shoul use a class...
    # init the game with raven/fruit/dice/player number. The player number should be delieveried by user input.
    def __init__(self, num_players):
        self.fruits = {"Apple": 10, "Banana": 10, "Cherry": 10, "Grape": 10}  #set fruits
        self.raven_position = 0  # raven position init
        self.max_raven_steps = 9  # raven's end
        # use for loop to set players in 
        self.players = [f"Player {i+1}" for i in range(num_players)]
        self.dice_faces = [1, 2, 3, 4, 5, 6]  # dice list / yeah , better use a list 
        self.current_player_index = 0  # user index
    # use a function with random to random get a number from dice list.
    def roll_dice(self):
        # use random to roll dice
        return random.choice(self.dice_faces)
    
    def remove_fruit(self, fruit):
        # only delete when there is still the right fruit left in the basket
        if self.fruits[fruit] > 0:
            self.fruits[fruit] -= 1
            print(f"{self.players[self.current_player_index]} removed one {fruit}. Remaining: {self.fruits[fruit]}")
        else:
            print(f"{self.players[self.current_player_index]} failed to remove {fruit}. because there is no one left")
    #
    def remove_two_random_fruits(self):
        #find the fruits which is still available for remove. This can achive 'move any fruit in the basket'
        available_fruits = [fruit for fruit, count in self.fruits.items() if count > 0]
        # if still have 2 kinds of fruit left in basket
        if len(available_fruits) >= 2:
            # random choose two and save the result in chosen_fruits
            chosen_fruits = random.sample(available_fruits, 2)
        elif len(available_fruits) == 1:
            # if only one kind of fruit left,choose it twice. no matter how many left ,because it's the only kind can remove.
            chosen_fruits = [available_fruits[0], available_fruits[0]]  
        else:
            return  # no available fruit
        # delete chosing fruit
        for fruit in chosen_fruits:
            self.remove_fruit(fruit)
    #
    def move_raven(self):
        print(f"{self.players[self.current_player_index]} roll a dice for 6 ")
        self.raven_position += 1
        # move the raven , show the raven's path.
        print(f"Raven moves forward! Position: {self.raven_position}/{self.max_raven_steps}")
    # check the game status 
    def check_game_over(self):
        if all(count == 0 for count in self.fruits.values()):
            # Ending 1: if all fruit.value =0 , end the game , player win 
            print("\nAll fruits have been taken! Players win! 🎉")
            return True
            # Ending 2: if the raven arrived 9 , end the game , raven win.
        if self.raven_position == self.max_raven_steps:
            print("\nRaven reached the end! Raven wins! 🦅")
            return True
        #else , keep running the game.
        return False

    def play_game(self):
        # the main function of this class
        print("\n🍎🍌🍒🍇 Welcome to the Raven-Fruit Game! 🍎🍌🍒🍇\n")
        while True:
            # always run the next round before break by the check function.
            player = self.players[self.current_player_index]
            # move the player to next player    
            dice_result = self.roll_dice()
            # get the dice result by roll_dice

            if 1 <= dice_result <= 4:
                # for dice_result in 1-4, delete corresponding fruit
                fruit_name = list(self.fruits.keys())[dice_result - 1]
                self.remove_fruit(fruit_name)
                # for dice_result =5 , call function remove 2 
            elif dice_result == 5:
                self.remove_two_random_fruits()
                # for dice_result =6 , call function raven
            elif dice_result == 6:
                self.move_raven()
            #after operation of this round , check if the game ends.
            if self.check_game_over():
                break

            # move to next player
            self.current_player_index = (self.current_player_index + 1) % len(self.players)


# get number of players 
num_players = int(input("Enter number of players: "))
# delievery the input number to init the game
game = FruitGame(num_players)
# use the play.game func in game class to run the game.
game.play_game()