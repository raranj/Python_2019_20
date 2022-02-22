from turtle import*
from time import*

t = Turtle()
t.pencolor('purple')
t.fillcolor('blue')
t.speed(0)
dir = 0;

for x in range(50):
    t.clear()
    t.setheading(0)
    t.penup()
    t.hideturtle()
    t.dot(75)
    t.forward(5)
    t.setposition(0,0)
    dir = dir + 4

print("done")
