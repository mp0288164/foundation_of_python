import turtle 
rb=turtle.Turtle()
rb.pensize(10)

def rainbow(col,rad,val):
    rb.color(col)
    rb.circle(rad,-180)
    rb.penup()
    rb.setpos(val,0)
    rb.pendown()
    rb.right(180)
col=['violet','indigo','blue','green','yellow','orange','red']
rb.right(90)
rb.width(10)
rb.speed(7)
for i in range(7):
    rainbow(col[i],10*(i+8),-10*(i+1))
turtle.done()

