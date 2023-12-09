# Author : Aman Anil Deshmukh & Sakshi Pawar
# Date : 3 December 2023
# Description: Snake class is created to define symbol "S", x and y coordinates on field
from Creature import Creature

class Snake(Creature):
    """Derived class from Creatures and defining x and y coordinates
        with Snake symbol "S" by calling its superclass constructor """
    def __init__(self, x, y):
        super().__init__(x, y, 'S')