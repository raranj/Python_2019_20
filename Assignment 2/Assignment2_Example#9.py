from turtle import * #import the turtle library
from time import * #import the time library

t = Turtle() #set the first pen name to t
t1 = Turtle() #set the second pen name to t1
t.speed(0) #set the first pen to the fastest speed
t.hideturtle() #hide the first pen from sight

x = 20 #set x to 20(variable is not being used)
t.pencolor('red') #set the first pen's color to red
t.dot(50) #draw a dot with the first pen with a radius of 50

t.penup() #lift the first pen so it doesn't draw
t.setposition(0, -200) #set the first pen's position to (0,-200)
t.pendown() #put the first pen down so that it can draw
t.pencolor('blue') #set the first pen's color to blue

t1.hideturtle() #hide the second pen from view
t1.penup() #lift the second pen so that it can't draw
t1.setposition(0, -250) #set the second pen's position to (0, -250)
t1.pendown() #put the second pen down so that it can draw
t1.pencolor('green') #set the second pen color to green

for y in range(200): #repeat the following 200 times:
    t.circle(200,2) #draw a circle with a radius of 200 for an extent of 2
    t.dot(5) #draw a dot with a radius of 5
    t1.circle(250,5) #draw a circle with a radius of 250 for an extent of 5
    t1.dot(10) #draw a dot with a radius of 10
    sleep(.5) #pause for 0.5 seconds
print ('Done') #print 'Done' when the program is finished

#This program is supposed to draw 2 rings of dots around one center dot
