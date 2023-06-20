from Spieler import Spieler
from Geist import Geist

class Spielfeld():
    def __init__(self, geist1, spieler1, x, y):
        self.__geist1 = geist1
        self.__spieler1 = spieler1
        self.__y = y
        self.__x = x
        self.__liste1 = []
        self.__liste2 = []
        self.spielfeld_erstellen( x, y)
        self.spielfeld_anzeigen(y)
        
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y

    def spielfeld_erstellen(self, x, y):        
        for i in range(y):
            self.__liste1.append(i)
            for j in range(x):
                self.__liste2.append(" ")
            self.__liste1[i] = self.__liste2
            self.__liste2 = []
        

    def spielfeld_anzeigen(self, y):
        self.__liste1[self.__spieler1.getAltPosY()][self.__spieler1.getAltPosX()]= ""        
        self.__liste1[self.__spieler1.getPosY()][self.__spieler1.getPosX()] = self.__spieler1._aussehen
        self.__liste1[self.__geist1.getAltPosY()][self.__geist1.getAltPosX()]= ""
        self.__liste1[self.__geist1.getPosY()][self.__geist1.getPosX()] = self.__geist1._aussehen
        for i in range(y):
            print(self.__liste1[i])
