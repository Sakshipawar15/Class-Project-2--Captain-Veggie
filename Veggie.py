from FieldInhabitant import FieldInhabitant
class Veggie(FieldInhabitant):
    def __init__(self, G, name, points):
        super.__init__(G)
        self._vegetablename = name
        self._points = points

    def __str__(self):
        return f"Symbol: {self._veggie}, Name: {self._vegetablename}, Points: {self._points}"

    def getvegetablename(self):
        return self._vegetablename

    def setvegetablename(self,name):
        self._vegetablename = name

    def getpoints(self):
        return self._points

    def setpoints(self, points):
        self._points = points