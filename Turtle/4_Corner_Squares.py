from turtle import*

def drawrectangle(fill,pen,length,width):
    pencolor(pen)
    fillcolor(fill)
    begin_fill()
    forward(length)
    left(90)
    forward(width)
    left(90)
    forward(length)
    left(90)
    forward(width)
    end_fill()

penup()
goto(-500,-500)
pendown()
drawrectangle('red', 'black', 300, 200)

penup()
goto(200,-200)
pendown()
drawrectangle('orange', 'black', 300, 300)

penup()
goto(500,500)
pendown()
drawrectangle('green','black',200,100)

penup()
goto(-300,300)
pendown()
drawrectangle('purple','black',200,200)
hideturtle()
