class Spielfigur():
    def __init__(self, name, aussehen, position_x, position_y):
        self._name = name,
        self._aussehen = aussehen
        self._position_x = position_x
        self._position_y = position_y
        self._position_x_alt = self._position_x
        self._position_y_alt = self._position_y

    def bewegen(self, parameter, spielfeld):
        if parameter == "d" or parameter == 0:
            if self._position_x == spielfeld.getX()-1:
                self._position_x = 0
            else:
                self._position_x += 1
        elif parameter == "a" or parameter == 1:
            if self._position_x == 0:
                self._position_x = spielfeld.getX()-1
            else:
                self._position_x -= 1
        elif parameter == "w" or parameter == 2:
            if self._position_y == 0:
                self._position_y = spielfeld.getY()-1
            else:
                self._position_y -= 1
        elif parameter == "s" or parameter == 3:
            if self._position_y == spielfeld.getY()-1:
                self._position_y = 0
            else:
                self._position_y += 1
                
    def geistBewegung(self, spieler, spielfeld):
        xDif = self._position_x - spieler._position_x
        yDif = self._position_y - spieler._position_y

        if xDif < 0:
            self.bewegen("d", spielfeld)
        elif xDif > 0:
            self.bewegen("a", spielfeld)
        elif yDif < 0:
            self.bewegen("s", spielfeld)
        elif yDif > 0:
            self.bewegen("w", spielfeld)

    def getPosX(self):
        return self._position_x

    def getAltPosX(self):
        return self._position_x_alt
    
    def getPosY(self):
        return self._position_y
    
    def getAltPosY(self):
        return self._position_y_alt