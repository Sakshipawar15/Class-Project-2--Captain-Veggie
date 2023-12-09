#Author : Aman Anil Deshmukh & Sakshi Pawar
#Date : 22nd November 2023
#Description: This class is a base class for symbols of objects
#             that are used in game and its getter and setter functions.

class FieldInhabitant:
    """Defining base class for object
        inhabitants in the field"""
    def __init__(self, symbol):
        self._symbol = symbol

    def get_symbol(self):
        return self._symbol

    def set_symbol(self, symbol):
        self._symbol = symbol