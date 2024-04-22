import turtle
star=turtle.Turtle()
star.pensize(10)
star.color('blue','cyan')
star.right(75)
star.forward(100)
star.speed(1)
star.begin_fill()
for i in range(4):
    star.right(144)
    star.forward(100)
star.end_fill()
turtle.done()
