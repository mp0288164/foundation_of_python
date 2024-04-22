from turtle import *
# face
pensize(10)
fillcolor('yellow')
hideturtle()
redius=180
penup()
setposition(0,-redius)
setheading(10)
pendown()
begin_fill()
circle(redius)
end_fill()

# mouth
mouth_redius=redius*0.6
mouth_angle=70
penup()
setposition(0,-mouth_redius)
setheading(0)
pendown()
circle(mouth_redius,mouth_angle)

penup()
setposition(0,-mouth_redius)
setheading(0)
pendown()
circle(mouth_redius,-mouth_angle)

def eye(eye_x,eye_y,eye_size):
    
    penup()
    setposition(-eye_x,eye_y)
    pendown()
    dot(eye_size)
    penup()
    setposition(eye_x,eye_y)
    pendown()
    dot(eye_size)
    done()
eye(50,50,60)
