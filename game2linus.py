from gturtle import * 
from random import randint
import time as t

CELLSIZE = 30
greyBlocks = randint(7, 25)
blockCount = 0
spiderSteps = 0

def getPoints(tokens):
    return 110 - (tokens * 10)


# Zeichnet das Grundgitter: 
def drawGrid():    
    global CELLSIZE     
    hideTurtle()     
    setPenColor("gray")    
    x = -400    
    for i in range((800 // CELLSIZE) + 1):  
      setPos(x, -300)    
      moveTo(x, +300)     
      x += CELLSIZE   
    y = -300    
    for j in range((600 // CELLSIZE) + 1):         
        setPos(-400, y)         
        moveTo(+400, y)        
        y += CELLSIZE
    
    # Zeichnet den Rand
    setPenColor("black")
    setPenWidth(CELLSIZE + 20)     
    setPos(-400, 300)
    moveTo(-400, -300)
    moveTo(400, -300)
    moveTo(400, 300)
    moveTo(-400, 300)
    
    # Zeichnet die grauen Blöcke ein
    setFillColor("grey")
    for _ in range(greyBlocks):
        x = randint(-370, 370)
        y = randint(-270, 270)
        
        setPos(x, y)
        fill()
            
    showTurtle()
    
#def path():
#    forward(CELLSIZE)
#    right(180)
#    forward(CELLSIZE)
#    penUp()
#    right(180)
#    for _ in range(setPenColor("yellow"):
#    setPenWidth(CELLSIZE)
#    pd()):
#        forward(CELLSIZE)
#    penDown()

def doStep():
    global spiderSteps    
    hideTurtle()    
    # Einen Schritt nach vorne machen.    
    forward(CELLSIZE)
    spiderSteps += 1
#    path()
    #gelbes Strich ziehen
#    setPenColor("yellow")
#    setPenWidth(CELLSIZE)
#    pd()
    
       
    # Falls die Turtle auf einem schwarzen Feld landet,  
    # setzen wir sie wieder zurück und drehen sie dafür.    
    if getPixelColorStr() == "black":        
        back(CELLSIZE)       
        right(90)
    elif getPixelColorStr() == 'gray':
        back(CELLSIZE)
        right(90)
    elif getPixelColorStr() == 'yellow':
        back(CELLSIZE)
        right(90)
    elif getPixelColorStr() == 'red':
        end = t.time()
        diff = end - start
        print("DU HAST GEWONNEN!")
        print("genutzte Blöcke: " + str(blockCount))
        print("gelaufene Felder:" + str(spiderSteps))
        print("Zeit: " + str(round(diff, 2)) + "s")
        print("Punkte:" + str(getPoints(blockCount)))
        putSleep()
           
    showTurtle() 
    
    

    ### ----------------------- MAIN --------------------------- ### 
makeTurtle('sprites/spider.png') 
drawGrid() 
definedTarget = False

# An dieser Stelle könntest du ein Feld als Ziel färben.
@onMouseHit
def defineTarget(x, y):
    global definedTarget, blockCount
    turtle_x = getX() 
    turtle_y = getY() 
    
    if definedTarget:    
        hideTurtle()    
        setPos(x, y)    
        if getPixelColorStr() == "white":       
            setFillColor("black")      
            fill(x, y)
            blockCount += 1
        elif getPixelColorStr() == "black":
            setFillColor("white")
            fill(x, y)
            blockCount += 1
        
        # Die Turtle wieder dahin zurücksetzen, wo sie vorher war.    
        setPos(turtle_x, turtle_y)    
        showTurtle()
    else:
        hideTurtle()    
        setPos(x, y)    
        if getPixelColorStr() == "white":       
            setFillColor("red")      
            fill(x, y)
        else:
            pass
        definedTarget = True   
            # Die Turtle wieder dahin zurücksetzen, wo sie vorher war.    
        setPos(turtle_x, turtle_y)    
        showTurtle()
    
    
# Die Turtle auf ein Anfangsfeld setzen: 
setPos(-400 + 5 * CELLSIZE // 2, -300 + 5 * CELLSIZE // 2)
penUp() 
lim = 1000
start = t.time() 
right(90)  
for k in range(lim):
    doStep()  
    delay(500)