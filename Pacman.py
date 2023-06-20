from Geist import Geist 
from Spieler import Spieler 
from Spielfeld import Spielfeld 

class Pacman():
    geist = Geist("geist","geist",0 ,3)
    spieler = Spieler("jakob","pacman",2,2)
    while not (geist.getPosX() == spieler.getPosX() and geist.getPosY() == spieler.getPosY()):       
        spielfeld = Spielfeld(geist,spieler,10,10) 
        spieler.bewegen(input(), spielfeld)
        geist.geistBewegung(spieler, spielfeld)
        
    else:
        print(f"YOU LOSE! spieler X: {spieler.getPosX()} spieler Y: {spieler.getPosY()} Geist X: {geist.getPosX()} Geist Y: {geist.getPosY()}")