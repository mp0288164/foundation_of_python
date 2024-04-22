import turtle
def move_obj(heart):
    heart.color('red','red')
    heart.begin_fill()
    heart.down()
    def curve():
        for i in range(200):
            heart.right(1)
            heart.forward(1)
    heart.left(140)
    heart.forward(113)
    curve()
    heart.left(120)
    curve()
    heart.forward(112)
    heart.end_fill()
    

#main code
if __name__ == "__main__":
    scr=turtle.Screen()
    scr.setup(650,650) #scr.setup(width,height)
    scr.bgcolor('lightblue')
    scr.tracer(0)
    heart=turtle.Turtle()
    heart.color('red')
    heart.speed(0)
    heart.width(2)
    heart.hideturtle()
    heart.penup()
    heart.goto(-350,0)
    heart.pendown()
    i=0
    while i<=10000:
        heart.clear()
        move_obj(heart)
        scr.update()
        heart.forward(0.1)
        i+=1
turtle.down()