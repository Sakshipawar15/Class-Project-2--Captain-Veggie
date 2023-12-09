# Author : Aman Anil Deshmukh & Sakshi Pawar
# Date : 22nd November 2023
# Description: Rabbit class is created to define symbol "R", x and y coordinates on field
from Creature import Creature
class Rabbit(Creature):
    """Derived class from Creatures and defining x and y coordinates
        with Rabbits symbol "R" by calling its superclass constructor """
    def __init__(self, x, y):
        super().__init__(x, y, "R")