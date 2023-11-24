#Author : Aman Anil Deshmukh & Sakshi Pawar
#Date : 22nd November 2023
#Description: Creating functions initVeggies(),initCaptain(),& initRabbits() to support the game.

import os
import random

def initveggies():
    vfile_name = input("Enter the name of the Veggie file: ")

    while not os.path.exists(vfile_name):
        vfile_name = input("oops!!! That file does not exists!! Please enter the name of the correct file: ")

    with open(vfile_name,'r') as file:
        first_line = file.readline().strip().split()
        print(first_line)

        rows = 10
        cols = 10


        veggie_list = [[None for i in range(cols)] for h in range(rows)]
        for col in zip(*veggie_list):
            print(col)

        veggies = []              #reading the remaining lines in the files to create new Veggie objects
        for line in file:
            veggie_data = line.strip().split()
            if len(veggie_data) == 3 and veggie_data[2].isdigit():
                veggie_name,veggie_abbreviation,veggie_quantity = veggie_data
                veggies.append(Veggie(veggie_name,veggie_abbreviation,int(veggie_quantity)))

        no_of_veggies = min(len(veggies),rows*cols)   # minimum number of veggies

        for _ in range(no_of_veggies):
            Veggie = random.choice(veggies)

            while True:
                row = random.randint(0,rows - 1)
                col = random.randint(0,cols - 1)

                if veggie_list[row][col] is None:
                    veggie_list[row][col] = Veggie
                    break
                print(veggies)


    print(f"selected Veggie file: {vfile_name}")
    return vfile_name

def main():
    initveggies()

if __name__ == '__main__':
    main()