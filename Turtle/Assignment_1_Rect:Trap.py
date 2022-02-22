from turtle import*

t = Turtle()

#Center Rectangle
t.screen.colormode(255)
t.pencolor(70, 107, 139)
t.fillcolor(124, 181, 230)
t.begin_fill()
t.forward(350)
t.left(90)
t.forward(200)
t.left(90)
t.forward(350)
t.left(90)
t.forward(200)
t.end_fill()

#Lightest Colored Trapezoid
t.fillcolor(183, 214, 240)
t.begin_fill()
t.goto(-30,-30)
t.goto(-30,230)
t.goto(0,200)
t.end_fill()

#Second Lightest Trapezoid
t.fillcolor(129, 177, 219)
t.begin_fill()
t.goto(-30,230)
t.goto(380,230)
t.goto(350,200)
t.end_fill()

#Darkest Trapezoid
t.fillcolor(78, 104, 127)
t.begin_fill()
t.goto(380,230)
t.goto(380,-30)
t.goto(350,0)
t.end_fill()

#Third Lightest Trapezoid
t.fillcolor(109, 149, 185)
t.begin_fill()
t.goto(380,-30)
t.goto(-30,-30)
t.goto(0,0)
t.end_fill()
t.hideturtle()



