import random

NUMBEROFVEGGIES = 30
NUMBEROFRABBITS = 5
HIGHSCOREFILE = "highscore.data"
class Gameengine:
    def __init__(self):

        self.__field = []
        self.__rabbits = []
        self.__captain = None
        self.__veggies = []
        self.__score = 0

    def initCaptain(self):
        x = random.randint(0,len(self.__field))  #grid size
        y = random.randint(0,len(self.__field[0]))

        while True:
            if self.__field is None:
                self.__captain = (x,y)
                self.__field[x][y] = self.__captain
