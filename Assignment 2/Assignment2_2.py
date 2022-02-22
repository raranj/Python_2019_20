from turtle import*
from time import*
import random

t = Turtle()
t.screen.colormode(255)

#Drawing a Star
def drawstar():
    xc = t.xcor()
    yc = t.ycor()
    t.begin_fill()
    t.forward(20)
    t.left(72)
    t.forward(20)
    t.right(144)
    t.forward(20)
    t.left(72)
    t.forward(20)

    t.right(144)

    t.forward(20)
    t.left(72)
    t.forward(20)
    t.right(144)
    t.forward(20)
    t.left(72)
    t.forward(20)

    t.right(144)

    t.forward(20)
    t.left(72)
    t.goto(xc,yc)
    t.end_fill()
    
for x in range(20):
    #Generating Random Coordinates, Colors, and Directions
    for x in range(20):
        x = random.randint(-300,301)
        y = random.randint(-300,301)

        rr = random.randint(0,255)
        gg = random.randint(0,255)
        bb = random.randint(0,255)
        
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
    
        h = random.randint(0,361)

    #Drawing Random Stars    
    #t.clear()
    t.penup()
    t.setposition(x,y)
    t.pendown()
    t.setheading(h)
    t.pencolor(rr,gg,bb)
    t.fillcolor(r,g,b)
    drawstar()
    sleep(1)

t.hideturtle()
    




