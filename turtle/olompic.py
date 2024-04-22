import turtle
t=turtle.Turtle()
t.pensize(5)
t.speed(10)
def olomp(x,y,col1,col2):
    t.penup()
    t.goto(x,y)
    t.color(col1,col2)
    t.pendown()
    t.begin_fill()
    t.circle(50)
    t.end_fill()

olomp(-100,25,'black','black')
olomp(10,25,'blue','blue')
olomp(120,25,'red','red')
olomp(-50,-20,'green','green')
olomp(60,-20,'yellow','yellow')
turtle.done()