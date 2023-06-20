from Spielfigur import Spielfigur

class Spieler(Spielfigur):
    def __init__(self, name, aussehen, position_x, position_y):
       Spielfigur.__init__(self, name, aussehen, position_x, position_y)

