# Author : Aman Anil Deshmukh & Sakshi Pawar
# Date : 22nd November 2023
# Description: This class defined to define and retrieve the location of objects on the field
from FieldInhabitant import FieldInhabitant
class Creature(FieldInhabitant):
    """Derived class from Field Inhabitant and
    defining the location of creatures on field"""
    def __init__(self, x, y, symbol):
        super().__init__(symbol)
        # Coordinates representing creatures
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y