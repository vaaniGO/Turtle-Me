import turtle
import math
t = turtle.Turtle()
t.shape("turtle")
t.speed(0)
t.color('red')
t.pensize(4)
# We start with an elementary circle which forms the circle-shaped hole in the centre
# Then, we take two diametrically opposite points along x=0. The way the Ashoka logo is made is that the x-axis bisects the two arcs
# such that deviating 180/10 on either side gives us the starting point of the first arc, then we increment by 180/5 to get to the point of the next arc and so on

def drawCircle(x, y, shiftx, shifty, radius):
  t.pendown()
  t.circle(radius)
  t.penup()
  t.goto(x-shiftx+radius, y-shifty+radius)
  t.pendown()
  t.circle(radius)

def drawReflectedCircle(x, y, radius):
  t.pendown()
  t.circle(radius)
  t.penup()
  t.goto(-x, -y)
  t.pendown()
  t.right(180)
  t.circle(radius)

def forwardAlongAxis():  
  t.left(90)
  t.penup()
  t.forward(100*(math.tan(math.pi / 10)))
  t.right(90)
  t.pendown() 

t.penup()
t.goto(0, 0)
t.goto(0, -100)
t.pendown()
t.circle(100)
t.penup()
t.goto(100, 0)
t.setheading(90)
t.penup()

for i in range(0, 10):
  t.penup()
  t.goto(0, 0)
  t.setheading(90)
  t.left(18 + i*180/5)
  t.forward(100)
  x = t.xcor()
  y = t.ycor()
  t.goto(x, y)
  t.left(90)
  t.pendown()
  drawReflectedCircle(x, y, 200)


t.penup()
t.goto(0, -100*math.sqrt(9))
t.pendown()
t.setheading(90)
t.right(90)
t.circle(100*math.sqrt(9))
#  145 173 207 242 272
t.penup()
t.goto(200, 200*(math.tan(math.pi / 10)))
t.left(108)
t.pendown()
t.circle(207)

forwardAlongAxis()
t.circle(173)
forwardAlongAxis()
t.circle(145)

t.penup()
t.goto(200, 200*(math.tan(math.pi / 10)))
t.right(90)
t.forward(28)
t.pendown()
t.left(90)
t.circle(242)
t.right(90)
t.penup()
t.forward(100*(math.tan(math.pi / 10)))
t.pendown()
t.left(90)
t.circle(272)
turtle.exitonclick()