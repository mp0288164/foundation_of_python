import turtle
#set background
scr=turtle.Screen()
ttl=turtle.Turtle()
scr.bgcolor('black')
#bottom line
ttl.penup()
ttl.goto(-170,-180)
ttl.color('white')
ttl.pendown()
ttl.forward(350)

#midline
ttl.penup()
ttl.goto(-160,-150)
ttl.color('white')
ttl.pendown()
ttl.forward(300)

#first line

ttl.penup()
ttl.goto(-150,-120)
ttl.pendown()
ttl.forward(250)

#cake
ttl.penup()
ttl.goto(-100,-100)
ttl.color('white')
ttl.begin_fill()
ttl.pendown()
ttl.forward(140)
ttl.left(90)
ttl.forward(95)
ttl.left(90)
ttl.forward(140)
ttl.right(-90)
ttl.forward(95)

#candles

ttl.penup()
ttl.goto(-90,0)
ttl.color("red")
ttl.left(180)
ttl.pendown()
ttl.forward(20)
def can(x,y,col):
    ttl.penup()
    ttl.goto(x,y)
    ttl.color(col)
    ttl.pendown()
    ttl.forward(20)
can(-60,0,'blue')
can(-30,0,'yellow')
can(0,0,'green')
can(30,0,'purple')

#decoration
colors=['red','orange','yellow','green','blue','purple','black']
ttl.penup()
ttl.goto(-40,-50)
ttl.pendown()
for each_color in colors:
    angle=360/len(colors)
    ttl.color(each_color)
    ttl.circle(10)
    ttl.forward(10)

turtle.done()    



