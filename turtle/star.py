import turtle 
star=turtle.Turtle()
star.pensize(5)
star.speed(1)
star.color('yellow','blue')
star.begin_fill()
for i in range(5):
    star.forward(50)
    star.right(120)
    star.forward(50)
    star.right(-48)#72-120=-48
star.end_fill()
turtle.done()