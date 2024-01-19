import turtle
import time
Size=2
x,y= turtle.position()
turtle.penup()
turtle.setposition(x,y-Size*85)
turtle.pendown()
turtle.color("red")
turtle.begin_fill()
turtle.pensize(3)
turtle.left(50)
turtle.forward(133*Size)
turtle.circle(50*Size,200)
turtle.right(140)
turtle.circle(50*Size,200)
turtle.forward(133*Size)
turtle.end_fill()
time.sleep(5)