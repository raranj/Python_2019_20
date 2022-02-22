from turtle import * #import turtle library
from time import * #import time library

t = Turtle() #t is a variable representing the pen
t.speed(0) #setting the pen's speed to the fastest one
t.hideturtle() #hiding the pen
x = 20 #variable x is used to represent the position of pen
t.pencolor('red') #setting the pen's color to red
t.fillcolor('blue') #setting the color filling to blue

for y in range(25): #for loop that runs 25 times
    t.penup() #lift the pen so it doesn't write
    x = x + 5 #increment the position by 5
    t.setposition(-x,-x) #move the pen over to the coordinates(-x,-x)
    t.pendown() #put the pen down so it can write
    t.begin_fill() #start filling
    for i in range(4): #do the following 4 times:
        t.forward(2 * x + 10) #move forward by (2 * x + 10)
        t.left(90) #turn left by 90 degrees
    t.end_fill() #stop filling
    sleep(.5) #pause for 0.5 seconds

print('Done') #print 'done' once program is finished

#This program is supposed to give the illusion that the rectangle is expanding by adding a box around the original and filling it in
