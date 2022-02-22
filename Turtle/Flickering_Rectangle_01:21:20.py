from turtle import*
from time import*

t = Turtle()
t.pencolor('red')
t.fillcolor('yellow')
t.speed(0)
dir = 0;
t.hideturtle()

for x in range(91):
    t.clear()
    t.setheading(dir)
    t.begin_fill()
    t.forward(200)
    t.left(90)
    t.stamp()
    t.forward(20)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.end_fill()
    t.setposition(0,0)
    sleep(1)
    dir = dir - 4

print('Done')
