from turtle import *
shape('turtle')
speed(5)
pensize(1) 
setheading(0)
def flow(right_angle1,circle_angle1,right_angle2,circle_angle2):
    #RIGHT LEAF
    penup()
    setposition(0,0)
    right(right_angle1)
    color('blue','aqua')
    pendown()
    begin_fill()
    circle(100,circle_angle1)
    end_fill()
    # LEFT LEAF
    penup()
    setposition(0,0)
    right(right_angle2)
    color('blue','green')
    pendown()
    begin_fill()
    circle(100,circle_angle2)
    end_fill()

flow(-150,-90,180,90)
flow(-0,-90,180,90)
flow(80,-90,180,90)
flow(380,-90,180,90)

done()