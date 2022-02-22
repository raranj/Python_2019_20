from turtle import*

t = Turtle()

#Moving the Pen
t.penup()
t.goto(-200,0)
t.pendown()

#Setting the Colors
t.screen.colormode(255)
t.pencolor(70, 107, 139)
t.fillcolor(124, 181, 230)

#Drawing the Star
t.begin_fill()
t.forward(200)
t.left(72)
t.forward(250)
t.right(144)
t.forward(250)
t.left(72)
t.forward(200)

t.right(144)

t.forward(200)
t.left(72)
t.forward(250)
t.right(144)
t.forward(250)
t.left(72)
t.forward(250)

t.right(144)

t.forward(250)
t.left(72)
t.goto(-200,0)
t.end_fill()
t.hideturtle()

