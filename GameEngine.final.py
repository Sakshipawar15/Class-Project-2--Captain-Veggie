# Author : Aman Anil Deshmukh & Sakshi Pawar
# Date : 26 November 2023
# Description: Game Engine an independent super class is defined which takes in other classes.
#              Functions for movement of field inhabitants in the 2D grid, recording scores in
#              file by pickling and displaying the same are defined in this file.

import os
import random
import pickle
from Veggie import Veggie
from Captain import Captain
from Rabbit import Rabbit

from FieldInhabitant import FieldInhabitant
from Creature import Creature
from Snake import Snake

class GameEngine:
    """Defining Functions required for game engine"""
    #Initializing private constants to start the game
    __NUMBER_VEGGIES = 30
    __NUMBER_RABBITS = 5
    #Initializing private constant to data file to store points
    __HIGHSCORE_FILE = "highscore.data"

    def __init__(self):
        self._field = []
        self._rabbits = []
        self._captain = None
        self._veggies = []
        self._score = 0
        self.snake = None


    def initVeggies(self):
        """Number of Vegetables is initialized to 30 and
        this function will take veggie data from csv input file and
        store the same to allocate random location for Vegetables in field"""
        filename = input("Enter veggie file name: ")
        while not os.path.exists(filename):
            print("File not found")
            filename = input("Enter veggie file name: ")

        with open(filename) as infile:
            lines = infile.readlines()
            first_line = lines[0]
            dimensions = first_line.strip().split(',')
            # Splitting the first line and splitting it based on comma
            # and taking indent 1 as height and 2 as width
            self.height = int(dimensions[1])
            self.width = int(dimensions[2])
            # Defining the field dimension based on above height and width
            # height, width = [int(x) for x in lines[0].strip().split(',')]
            self._field = [[None for _ in range(self.width)] for _ in range(self.height)]

            for line in lines[1:]:
                # Reading line after field from csv file, splitting it by comma
                # Storing Vegetable name in table along with its symbol and points
                data = line.strip().split(',')
                veggie = Veggie(data[0], data[1], int(data[2]))
                self._veggies.append(veggie)

        for _ in range(self.__NUMBER_VEGGIES):
            occupied = True
            while occupied:
                # choosing random location for x and y based on user enter height and width in csv file
                # lower limit is taken as zero and upper limit is taken and 1 is subtracted as line is
                # counted from 0. So this will choose a random 'x' and 'y' from 0 to upper limit.
                x = random.randint(0, self.width - 1)
                y = random.randint(0, self.height - 1)
                # To check if position is occupied by any other Vegetables on field.
                # If not then place a random vegetable from list
                if not self._field[y][x]:
                    self._field[y][x] = random.choice(self._veggies)
                    occupied = False

    def initCaptain(self):
        """this function will choose random location for Captain 'V' on
        field by checking if that location is not
        occupied by any other field inhabitants"""
        occupied = True
        while occupied:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self._field[y][x] is None:
                self._captain = Captain(x,y)
                self._field[y][x] = self._captain
                occupied = False
    def reinitCaptain(self,rem_veggie):
        """Additional function to reinitialize the captain where basket doesn't go to null and
        starts with previous veggies remaining in basket"""
        occupied = True
        while occupied:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self._field[y][x] is None:
                self._captain = Captain(x, y)
                self._field[y][x] = self._captain
                for i in range(len(rem_veggie)): # adding previous veggies after reducing latest 5 to basket
                    self._captain.addVeggie(rem_veggie[i])
                occupied = False

    def initRabbits(self):
        """Number of rabbits is initialized to 5 and
        this function will choose random location for rabbits on
        field by using same logic of whether any place is not
        occupied by any other (Veggies and Captain) field inhabitant"""
        for _ in range(self.__NUMBER_RABBITS):
            occupied = True
            while occupied:
                x = random.randint(0, self.width - 1)
                y = random.randint(0, self.height - 1)
                if self._field[y][x] is None:
                    rabbit = Rabbit(x, y)
                    self._rabbits.append(rabbit)
                    self._field[y][x] = rabbit
                    occupied = False

    def initSnake(self):
        """defines initial position of snake"""
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self._field[y][x] is None:
                self.snake = Snake(x, y)
                self._field[y][x] = 'S'
                break

    def initializeGame(self):
        """Calling init functions of all Field inhabitants to initialize the game"""
        self.initVeggies()
        self.initCaptain()
        self.initRabbits()
        self.initSnake()


    def remainingVeggies(self):
        """This function is defined to calculate remaining vegetables on field"""
        count = 0
        for row in self._field:
            for item in row:
                if isinstance(item, Veggie):
                    count += 1
        return count

    def intro(self):
        """Displaying description/ information regarding the game"""
        print("Welcome to Captain Veggie!")
        print("The rabbits have invaded your garden and you must harvest \nas many "
              "vegetables as possible before the rabbits eat them all!\n"
              "Each Vegetable is worth different point which is displayed \nbelow, "
              "So go for highest score!")
        print("The Vegetables in your garden are:")
        for veggie in self._veggies:
            print(veggie)
        print("Captain Veggie is V, and the rabbit's are R's")
        print("\nGoodluck!")

    def printField(self):
        """Function to print border that is twice the width above and below and
        also print at start and end of the field rows"""
        print("#" * (self.width * 2 + 2))
        for row in self._field:
            print("#", end="")
            for item in row:
                if isinstance(item, str):
                    symbol = item
                else:
                    symbol = " " if not item else item.get_symbol()
                print(f"{symbol} ", end="")
            print("#")
        print("#" * (self.width * 2 + 2))

    def getScore(self):
        """Getting and returning the current score"""
        return self._score

    def moveRabbits(self):
        """This function defines the rabbits movement randomly in field.
        This function will check if a location(x,y) is occupied by veggies,
        if rabbit moves on that location it will replace that veggie with rabbit
        showing that rabbit has eaten the vegetable."""
        for rabbit in self._rabbits:
            #Rabbits random movement
            move_x = random.choice([-1, 0, 1])
            move_y = random.choice([-1, 0, 1])
            x = rabbit.get_x() + move_x
            y = rabbit.get_y() + move_y

            if 0 <= x < len(self._field[0]) and 0 <= y < len(self._field):
                #If location occupied by vegetable and rabbit moves in tht location, rabbit will take that position
                if isinstance(self._field[y][x], Veggie):
                    self._field[rabbit.get_y()][rabbit.get_x()] = None
                    rabbit.set_x(x)
                    rabbit.set_y(y)
                    self._field[y][x] = rabbit
                    print("A rabbit ate a veggie!")

                elif not self._field[y][x]:
                    # If location is empty and rabbit moves in tht location, rabbit will take that position
                    self._field[rabbit.get_y()][rabbit.get_x()] = None
                    rabbit.set_x(x)
                    rabbit.set_y(y)
                    self._field[y][x] = rabbit

    def moveCptVertical(self, direction):
        """This Function will define vertical movement of captain"""
        x = self._captain.get_x()
        y = self._captain.get_y() + direction #captains up and down movement

        if 0 <= y < len(self._field):
            #If veggie is at the location where captain is moving
            if isinstance(self._field[y][x], Veggie):
                veggie = self._field[y][x]
                print(f"Yummy! A delicious {veggie.get_name()}")
                #Adding vegetable to the list
                self._captain.addVeggie(veggie)
                #adding points attached to it to the sum of scores
                self._score += veggie.get_points()
                self._field[self._captain.get_y()][x] = None
                #setting captain location to that of veggie
                self._captain.set_y(y)
                self._field[y][x] = self._captain
            # If no inhabitant just move vertically user prompted movement.
            elif not self._field[y][x]:
                self._field[self._captain.get_y()][x] = None
                self._captain.set_y(y)
                self._field[y][x] = self._captain
            else:
                print("Don't step on the bunnies!")

        else:
            print("You can't move that way!")

    def moveCptHorizontal(self, direction):
        """This Function will define horizontal movement of captain"""
        x = self._captain.get_x() + direction #captains left and right movement
        y = self._captain.get_y()

        if 0 <= x < len(self._field[0]):
            if isinstance(self._field[y][x], Veggie):
                veggie = self._field[y][x]
                print(f"Yummy! A delicious {veggie.get_name()}")
                # Adding vegetable to the list
                self._captain.addVeggie(veggie)
                # adding points attached to it to the sum of scores
                self._score += veggie.get_points()
                self._field[self._captain.get_y()][self._captain.get_x()] = None
                # setting captain location to that of veggie
                self._captain.set_x(x)
                self._field[y][x] = self._captain
            #If no inhabitant just move horizontally user prompted movement.
            elif not self._field[y][x]:
                self._field[self._captain.get_y()][self._captain.get_x()] = None
                self._captain.set_x(x)
                self._field[y][x] = self._captain

            else:
                print("Don't step on the bunnies!")

        else:
            print("You can't move that way!")


    def moveCaptain(self):
        """This Function controls the direction of captains movement based on user prompt
        W = Vertical -1 is up, S = vertical 1 is down, A = horizontal -1 is left
        and D = horizontal 1 is right. Anything other than WASD will display invalid action."""
        direction = input("[W]Up [S]Down [A]Left [D]Right: ").upper()

        if direction == "W": #Up move
            self.moveCptVertical(-1)

        elif direction == "S": #down move
             self.moveCptVertical(1)

        elif direction == "A": #Left move
            self.moveCptHorizontal(-1)

        elif direction == "D": #Right move
            self.moveCptHorizontal(1)

        else:
            print(f"{direction} is not a valid option")

    def moveSnake(self):
        """Defines snake movement on the field and function to check if snake has taken
        captain's location which means captain is bitten by snake and reduces 5 veggies
         captain's basket and reduces points for those vegetables"""
        if self.snake is None:
            return

        # Save prev positions
        prev_x = self.snake.get_x()
        prev_y = self.snake.get_y()

        prev_cap_x = self._captain.get_x()
        prev_cap_y = self._captain.get_y()

        move_x, move_y = 0, 0

        if self._captain.get_x() > self.snake.get_x():
            move_x = 1
        elif self._captain.get_x() < self.snake.get_x():
            move_x = -1

        if self._captain.get_y() > self.snake.get_y():
            move_y = 1
        elif self._captain.get_y() < self.snake.get_y():
            move_y = -1

        new_x = self.snake.get_x() + move_x
        new_y = self.snake.get_y() + move_y

        valid_moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        move_x = new_x - self.snake.get_x()  # Check if movement is valid
        move_y = new_y - self.snake.get_y()
        if (move_x, move_y) not in valid_moves:
            return
        if 0 <= new_x < len(self._field[0]) and 0 <= new_y < len(self._field):
            if not isinstance(self._field[new_y][new_x], (Veggie, Rabbit)):
                if new_x == self._captain.get_x() and new_y == self._captain.get_y():
                    print("Oh no! The snake has eaten Captain Veggie!")
                    print("Last 5 veggies will be removed.Continue collecting veggies")
                    #Removing veggies after snake bites the captain
                    removed_veggies = self._captain.remove_last_veggies(5)
                    for x in range(len(removed_veggies)):
                        print(removed_veggies[x])
                    pt = 0 #setting points of removed veggies to 0
                    for veggie in removed_veggies:
                        pt += veggie.get_points()  #adding points of removed veggies
                    self._score -= pt #subtracting total points of removed veggies from total score

                    # Clear previous captain position
                    self._field[prev_cap_y][prev_cap_x] = None
                    # Reset captain and snake
                    self.reinitCaptain(self._captain.get_basket()) #reinializing so basket will contain previous veggies too

                    self.initSnake()
                    # Clear previous snake position
                    self._field[prev_y][prev_x] = None

                else:
                    #Snake movement
                    self._field[self.snake.get_y()][self.snake.get_x()] = None
                    self.snake.set_x(new_x)
                    self.snake.set_y(new_y)
                    self._field[new_y][new_x] = 'S'
            else:
                pass
        else:
            pass

    def gameOver(self):
        """This function will display the Vegetables collected that is defined
        as basket and sum of scores for the vegetables collected"""
        print("GAME OVER!")
        print("You managed to harvest the following vegetables:")
        for veggie in self._captain.get_basket():
            print(veggie.get_name())
        print(f"Your score: {self.getScore()}")

    def highScore(self):
        """Pickling a file and loading and dumping used in this function to store initials
        and scores of the player """
        scores = [] #Empty List to store tuples
        try:
            with open(self.__HIGHSCORE_FILE, "rb") as file:
                scores = pickle.load(file)
        except:
            pass

        initials = input("Please enter your three initials to go on the scoreboard: ")[:3]
        #Create Tuple for player name and his associated score
        score = (initials.upper(), self.getScore())
        #Adding the tuple to score list
        scores.append(score)
        #Sorting data in descending order of scores
        def sortkey(x):
            return x[1]
        scores.sort(key=sortkey, reverse=True)

        #Displaying scores of all player stored in data file
        print("\nHIGH SCORES")
        print("------------------")
        print("Name	   Score")
        for score in scores:
            print(f"{score[0]:<5}  {score[1]:>5}")

        with open(self.__HIGHSCORE_FILE, "wb") as file:
            pickle.dump(scores, file)



