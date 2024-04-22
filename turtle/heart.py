import turtle
ttl=turtle.Turtle()
scr=turtle.Screen()
scr.bgcolor('light blue')
scr.setup(800,700)
ttl.pensize(5)
ttl.hideturtle()
#ttl._tracer(0)
ttl.speed(3)
ttl.color('navy')
ttl.penup()
ttl.setpos(-600,200)
ttl.pendown()
ttl.write("H",font=('verdana',60,'normal'))

ttl.penup()
ttl.setpos(-600,100)
ttl.pendown()
ttl.write("A",font=('verdana',60,'normal'))

ttl.penup()
ttl.setpos(-600,0)
ttl.pendown()
ttl.write("P",font=('verdana',60,'normal'))

ttl.penup()
ttl.setpos(-600,-100)
ttl.pendown()
ttl.write("P",font=('verdana',60,'normal'))

ttl.penup()
ttl.setpos(-600,-200)
ttl.pendown()
ttl.write("y",font=('verdana',60,'normal'))

ttl.penup()
ttl.setpos(-600,-300)
ttl.pendown()
ttl.write("B",font=('verdana',60,'normal'))

ttl.penup()
ttl.setpos(-500,-300)
ttl.pendown()
ttl.write("I",font=('verdana',60,'normal'))

ttl.penup()
ttl.setpos(-400,-300)
ttl.pendown()
ttl.write("R",font=('verdana',60,'normal'))
ttl.penup()
ttl.setpos(-300,-300)
ttl.pendown()
ttl.write("T",font=('verdana',60,'normal'))

ttl.penup()
ttl.setpos(-200,-300)
ttl.pendown()
ttl.write("H",font=('verdana',60,'normal'))

ttl.penup()
ttl.setpos(-100,-300)
ttl.pendown()
ttl.write("D",font=('verdana',60,'normal'))

ttl.penup()
ttl.setpos(0,-300)
ttl.pendown()
ttl.write("A",font=('verdana',60,'normal'))

ttl.penup()
ttl.setpos(100,-300)
ttl.pendown()
ttl.write("Y",font=('verdana',60,'normal'))

ttl.color('deep pink')
ttl.penup()
ttl.setpos(200,-300)
ttl.pendown()
ttl.write("MR.",font=('comic Sans Ms',60,'normal'))
ttl.penup()
ttl.setpos(-630,270)
ttl.pendown()
ttl.write('****************************************************',font=('courier',30,'normal'))
ttl.penup()
ttl.setpos(-630,-330)
ttl.pendown()
ttl.write('****************************************************',font=('courier',30,'normal'))
ttl.penup()
ttl.setpos(-50,-200)
ttl.color('navy')
ttl.speed(1)
ttl.pendown()
ttl.write("""Today is the birthday of the

Sweestest person on the earth.

I am so lucky to have you. 

HAPPY BIRTHDAY PARTNER.

You make my life complete......""",font=('comic Sans Ms',30,'italic'))



#ttl._tracer(0)
ttl.up()
ttl.setpos(-200,-100)
ttl.color('red','red')
ttl.begin_fill()
ttl.down()
def curve():
    for i in range(200):
        ttl.right(1)
        ttl.forward(1)
ttl.left(140)
ttl.forward(113)
curve()
ttl.left(120)
curve()
ttl.forward(112)
ttl.end_fill()

#_______left heart
ttl.up()
ttl.setpos(-400,0)
ttl.color('navy blue','navy blue')
ttl.begin_fill()
ttl.down()
def curve():
    for i in range(200):
        ttl.right(1)
        ttl.forward(1)
ttl.left(-80)
ttl.forward(110)
curve()
ttl.left(120)
curve()
ttl.forward(112)
ttl.end_fill()
ttl.color('navy') #turtle colors are yellow,gold,orange,red,maroon,voilet,magenta,
#purple,navy,blue,skyblue,cyan,turquoise,lightgreen,darkgreen,chocolate,brown,black,gray,whitee

"""
#cake
turtle.penup()
turtle.color('white')
turtle.setpos(200,-200)
turtle.right(90)
turtle.pendown()
turtle.forward(100)"""







turtle.done()

   
