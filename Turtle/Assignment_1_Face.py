from turtle import*

t = Turtle()

#Setting the Colors
t.screen.colormode(255)
t.pencolor(70, 107, 139)
t.fillcolor(124, 181, 230)

#Face
t.penup()
t.goto(0,-200)
t.pendown()
t.begin_fill()
t.circle(300)
t.end_fill()

#Eyes
t.penup()
t.goto(-115,200)
t.pendown()
t.dot(45)
t.penup()
t.goto(110,200)
t.pendown()
t.dot(45)

#Mouth
t.penup()
t.goto(-120,-40)
t.pendown()
t.setheading(320)
t.circle(175, 85)
t.hideturtle()



