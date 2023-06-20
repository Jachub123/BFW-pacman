# BEFEHLE:  kara.
#   move()  turnRight()  turnLeft()
#   putLeaf()  removeLeaf()
#
# SENSOREN: kara.
#   treeFront()  treeLeft()  treeRight()
#   mushroomFront()  onLeaf()
#

# hier können Sie eigene Methoden definieren

# hier kommt das Hauptprogramm hin, zB:
variable = tools.intInput("Bitte geben Sie eine Zahl ein! ")
i = 0
j = 1
turnCount = 0
outerFrame = True

while not kara.treeFront():
  if kara.onLeaf():
    break
  kara.putLeaf()
  kara.move()
  i += 1
  
  if outerFrame:
    if turnCount == 3:
      j += 1
      turnCount = 0
      outerFrame = False
  else:
      if turnCount == 2:
	    j += 1
	    turnCount = 0
    
  if i == variable-j:
    turnCount += 1
    kara.turnLeft()
    i = 0
    
        