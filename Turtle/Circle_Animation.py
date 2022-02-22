from turtle import*
from time import*

t = Turtle()
t.pencolor('red')
t.fillcolor('blue')
t.speed(0)
dir = 0;
x = 0
y = 0

for x in range(30):
    t.clear()
    t.penup()
    t.setposition(x,y)
    t.setheading(45)
    t.forward(100)
    t.right(100)
    t.hideturtle()
    x = x + 50
    y = y + 20
    t.hideturtle()
    t.setposition(x,y)
    t.dot(75)
    t.hideturtle()
    sleep(1)
    t.hideturtle()

print("Done")
