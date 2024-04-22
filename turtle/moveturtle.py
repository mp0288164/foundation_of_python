import turtle
def move_obj(ball):
    ball.fillcolor("yellow")
    ball.begin_fill()
    ball.circle(100)
    ball.end_fill()
    

#main code
if __name__ == "__main__":
    scr=turtle.Screen()
    scr.setup(650,650) #scr.setup(width,height)
    scr.bgcolor('lightblue')
    scr.tracer(0)
    ball=turtle.Turtle()
    ball.color('red')
    ball.speed()
    ball.width(2)
    ball.hideturtle()
    ball.penup()
    ball.goto(-350,0)
    ball.pendown()
    i=0
    while i<=10000:
        ball.clear()
        move_obj(ball)
        scr.update()
        ball.forward(0.1)
        i+=1
turtle.down()