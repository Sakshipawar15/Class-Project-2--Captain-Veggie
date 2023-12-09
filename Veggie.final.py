# Author : Aman Anil Deshmukh & Sakshi Pawar
# Date : 22nd November 2023
# Description: This is a derived class representing vegetable objects used in Field.
from FieldInhabitant import FieldInhabitant
class Veggie(FieldInhabitant):
    """Derived class from FieldInhabitant class where superclass constructor is called """
    def __init__(self, name, symbol, points):
        super().__init__(symbol)
        # Define new variables for Vegetables on field
        self._name = name
        self._points = points

    def __str__(self):
        """Function to output vegetable name, points and symbol"""
        return f"{self.get_symbol()} : {self._name} {self._points} points"

    def get_name(self):
        return self._name

    def get_points(self):
        return self._points

    def set_name(self, name):
        self._name = name

    def set_points(self, points):
        self._points = points