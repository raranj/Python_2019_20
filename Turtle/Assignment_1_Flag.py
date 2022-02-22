from turtle import*

#Drawing a Stripe
def drawstripe(pen,fill,y):
    pencolor(pen)
    fillcolor(fill)
    setheading(0)
    penup()
    goto(-500,y)
    pendown()
    begin_fill()
    forward(750)
    left(90)
    forward(30)
    left(90)
    forward(750)
    left(90)
    forward(30)
    end_fill()

#Drawing a Star
def drawstar():
    pencolor('white')
    fillcolor('white')
    begin_fill()
    forward(6)
    right(144)
    forward(6)
    right(144)
    forward(6)
    right(144)
    forward(6)
    right(144)
    forward(6)
    end_fill()

#Drawing a Line of Stars
def draw_line_of_stars(num):
    for i in range(num):
        
        drawstar()
        setheading(0)
        penup()
        forward(60)
        pendown()
    
#Drawing the Stripes
drawstripe('red','red',400)
drawstripe('white','white',370)
drawstripe('red','red',340)
drawstripe('white','white',310)
drawstripe('red','red',280)
drawstripe('white','white',250)
drawstripe('red','red',220)
drawstripe('white','white',190)
drawstripe('red','red',160)
drawstripe('white','white',130)
drawstripe('red','red',100)
drawstripe('white','white',70)
drawstripe('red','red',40)
hideturtle()

#Blue Background for Stars

t = Turtle()

t.penup()
t.goto(-500,430)
t.pendown()
t.setheading(270)
t.screen.colormode(255)
t.pencolor(24, 48, 142)
t.fillcolor(24, 48, 142)
t.begin_fill()
t.forward(210)
t.left(90)
t.forward(363)
t.left(90)
t.forward(210)
t.left(90)
t.forward(363)
t.end_fill()
t.hideturtle()

#Drawing the Stars

setheading(0)
penup()
goto(-475,410)
pendown()
draw_line_of_stars(6)

setheading(0)
penup()
goto(-450,390)
pendown()
draw_line_of_stars(5)

setheading(0)
penup()
goto(-475, 370)
pendown()
draw_line_of_stars(6)

setheading(0)
penup()
goto(-450, 350)
pendown()
draw_line_of_stars(5)

setheading(0)
penup()
goto(-475, 330)
pendown()
draw_line_of_stars(6)

setheading(0)
penup()
goto(-450, 310)
pendown()
draw_line_of_stars(5)

setheading(0)
penup()
goto(-475, 290)
pendown()
draw_line_of_stars(6)

setheading(0)
penup()
goto(-450, 270)
pendown()
draw_line_of_stars(5)

setheading(0)
penup()
goto(-475, 250)
pendown()
draw_line_of_stars(6)

hideturtle()





