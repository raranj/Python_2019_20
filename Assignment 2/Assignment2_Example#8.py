from turtle import * #import the turtle library
from time import * #import the time library

t = Turtle() #set the pen name to t
t.speed(0) #set the speed to the fastest possible
t.hideturtle() #hide the pen from view
x = 20 #start with a radius of 20
dir = 0 #set the direction to 0 at the beginning

for y in range(50): #do the following 50 times:
    t.penup() #lifting the pen so it doesn't write
    #t.clear() #clearing the screen every iteration(has been commented out)
    x = x + 5 #increment the radius by 5
    t.setposition(0,-x) #move the pen to the coordinates(0,-x)
    t.pendown() #put the pen down so that it can write
    t.pencolor('red') #set the pen's color to red
    t.fillcolor('blue') #fill with the color blue
    t.begin_fill() # start filling the circle
    t.circle(x) #draw a circle with radius x
    t.end_fill() #stop filling
    sleep(0.5) #pause for 0.5 seconds

print('Done') #printing "Done" when the program is finished
    
