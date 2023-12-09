# Author : Aman Anil Deshmukh & Sakshi Pawar
# Date : 22nd November 2023
# Description: Captain class is created to define symbol "V", x and y coordinates on field
# and vegetables collected by captain
from Creature import Creature
class Captain(Creature):
    """Derived class from Creatures and defining x and y coordinates
       with Captain symbol "V" by calling its superclass constructor """
    def __init__(self, x, y):
        super().__init__(x, y, "V")
        self._basket = []

    def addVeggie(self, veggie):
        """This function is to add vegetable to the
         list created as basket in the constructor"""
        self._basket.append(veggie)


    def remove_last_veggies(self, count):
        """Removing last 5 veggies from captains basket and storing it in list"""
        removed = []
        if count > len(self._basket):
            count = len(self._basket)
            print(f"Removing last {count} vegetables from the basket.")
        for _ in range(count):
            removed.append(self._basket.pop())
        return removed
    def get_basket(self):
        return self._basket

    def set_basket(self, basket):
        self._basket = basket