# Author : Aman Anil Deshmukh & Sakshi Pawar
# Date : 30 November 2023
# Description: Main function to run the Captain veggie game

from GameEngine import GameEngine
#VeggieFile1.csv
#VeggieFile2.csv

def main():
    """Main function calls all the functions necessary to run the game defined in Game Engine file"""
    game = GameEngine()
    game.initializeGame()
    game.intro()

    veggies_left = game.remainingVeggies()

    while veggies_left > 0:
        print(f"{veggies_left} veggies remaining. Current score: {game.getScore()} ")


        game.printField() #Prints field
        game.moveCaptain() #Moves captain vertically and horizontally
        game.moveRabbits() #Moves rabbits on random basis one space front, back, sideways and diagonally
        game.moveSnake() #moves snake front and back and functions to remove last 5 veggies

        veggies_left = game.remainingVeggies() #prints remaining vegetables

    game.gameOver()
    game.highScore()


main()