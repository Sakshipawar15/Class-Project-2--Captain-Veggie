from FieldInhabitant import FieldInhabitant
class Creature:
    def __init__(self, x, y, R, V):
        super.__init__(R,V)
        self._xcorr = x
        self._ycorr = y

    def getxcorr(self):
        return self._xcorr

    def getycorr(self):
        return self._ycorr

    def setxcorr(self,x):
        self._xcorr = x

    def setycorr(self,y):
        self._ycorr = y
