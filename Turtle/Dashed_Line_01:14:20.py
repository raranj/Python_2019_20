from turtle import*

def drawdashedline(t,length,dash):
    for y in range(int(length/(2*dash))):
        t.pendown()
        t.forward(dash)
        t.penup()
        t.forward(dash)

t = Turtle()
t.penup()
colormode(255)
t.pencolor(128,128,128)
t.setposition(-200,-100)
drawdashedline(t,400,10)
t.left(120)
drawdashedline(t,400,10)
t.left(120)
drawdashedline(t,400,10)

t.setposition(0,0)
drawdashedline(t,200,10)
t.left(144)
drawdashedline(t,200,10)
t.left(144)
drawdashedline(t,200,10)
t.left(144)
drawdashedline(t,200,10)
t.left(144)
drawdashedline(t,200,10)

