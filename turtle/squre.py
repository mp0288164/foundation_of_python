from turtle import *
t=turtle.Turtle()
s=int(input("enter the length of the side squre:- "))
col=input("enter the color name or hex value of color(# RRGGBB):-")
t.fillcolor(col)
t.begin_fill()

for i in range(4):
    t.forward(s)
    t.right(90)

t.end_fill()
turtle.done()