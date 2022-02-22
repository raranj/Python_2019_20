from turtle import*
from time import*

#Setting the Color and Speed
t = Turtle()
t.screen.colormode(255)
t.pencolor(52,96,129)
t.fillcolor(84,140,205)
t.speed(0)
t.hideturtle()

#Drawing a Rectangle
def drawrect(angle1):
    t.setheading(angle1)
    t.begin_fill()
    t.forward(210)
    t.left(90)
    t.forward(176)
    t.left(90)
    t.forward(210)
    t.left(90)
    t.forward(176)
    t.end_fill()

#Setting the Variables
angle = 45
angle1 = 180

#Rotating the Rectangle
for x in range(19):
    t.clear()
    t.setheading(angle)
    t.penup()
    t.forward(137)
    t.pendown()
    drawrect(angle1)
    angle1 = angle1 + 20
    angle = angle + 20
    sleep(1)
    t.penup()
    t.goto(0,0)
    t.pendown()
