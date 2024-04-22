from turtle import *
import turtle
tur=turtle.Screen()
tur.bgcolor("black")
tur.title("mypython")
turt=turtle.Turtle()
turt.color("white")
for i in range(4):
    turt.forward(100)
    turt.left(90)
turt.goto(50,50)
for i in range(4):
    turt.forward(100)
    turt.left(90)
turt.goto(150,50)
turt.goto(100,0)
turt.goto(100,100)
turt.goto(150,150)
turt.goto(50,150)
turt.goto(0,100)
done()