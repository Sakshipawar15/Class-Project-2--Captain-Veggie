from Creature import Creature
class Captain(Creature):
    def __init__(self, x, y):
        super().__init__(x, y, "V")
        self.veggies_collect = []

    def addveggies(self, veggie):
        self.veggies_collect.append(veggie)    #append the object

    def getveggies(self):
        return self.veggies_collect            #return the object

    def setveggies(self, V):
        self.veggies_collect = V