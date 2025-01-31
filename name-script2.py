import turtle
import math
t = turtle.Turtle()
t.shape("turtle")
t.speed(0)
t.pensize(8)

# Start at -200, 0
t.penup()
t.goto(-200, -100)
t.setheading(90)
t.right(60)
t.pendown()
t.circle(100, 65)
t.setheading(90)
t.left(90)
t.forward(100)
t.left(90)
t.forward(40)
t.penup()
t.goto(-200, 0)
t.setheading(90)
t.pendown()
t.forward(20)
t.penup()
t.backward(20)
t.right(90)
t.forward(50)
t.setheading(90)
t.pendown()
t.left(45)
t.forward(20)
t.right(90)
t.penup()
t.forward(10)
t.setheading(90)
t.left(45)
t.pendown()
t.backward(20)

# Second letter 
t.penup()
t.setheading(90)
t.right(90)
t.forward(30)
t.pendown()
t.forward(100)
t.right(90)
t.penup()
t.forward(50)
t.right(90)
t.forward(60)
t.setheading(90)
t.right(90)
t.pendown()
t.circle(60, 80)
t.penup()
t.setheading(90)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.pendown()
t.setheading(90)
t.right(90)
t.circle(70, 20)
t.circle(20, 50)
t.setheading(90)
t.forward(60)

# Third letter 
t.penup()
t.right(90)
t.forward(100)
t.pendown()
t.forward(70)

# # Fourth letter 
t.penup()
t.forward(10)
t.left(90)
t.forward(30)
t.pendown()
t.right(90)
t.forward(80)
t.penup()
t.forward(10)
t.right(90)
t.forward(60)
t.right(90)
t.pendown()
t.forward(100)

# Fifth letter
t.right(180)
t.penup()
t.forward(150)
t.left(90)
t.forward(30)
t.pendown()
t.dot(25)

# Sixth letter
t.penup()
t.right(90)
t.forward(40)
t.left(90)
t.forward(30)
t.pendown()
t.right(90)
t.forward(100)
t.right(90)
t.forward(120)
t.penup()
t.backward(20)
t.pendown()
t.right(90)
t.forward(100)
t.penup()
t.backward(100)
t.right(90)
t.forward(100)
t.setheading(90)
t.pendown()
t.left(45)
t.forward(20)
t.right(90)
t.penup()
t.forward(10)
t.setheading(90)
t.left(45)
t.pendown()
t.backward(20)
t.penup()
t.backward(10)

# Seventh letter
t.penup()
t.setheading(90)
t.right(90)
t.forward(10)
t.right(90)
t.forward(100)
t.left(90)
t.pendown()
t.forward(100)
t.penup()
t.backward(50)
t.left(90)
t.pendown()
t.forward(100)
t.left(90)
t.forward(40)
t.penup()
t.backward(40)
t.right(180)
t.pendown()
t.forward(60)

# Eighth letter
t.penup()
t.forward(60)
t.right(90)
t.forward(30)
t.right(90)
t.right(45)
t.pendown()
t.circle(140, 20)
t.penup()
t.setheading(90)
t.backward(100)
t.pendown()
t.right(75)
t.circle(120, 60)
t.setheading(90)
t.penup()
t.forward(20)
t.right(90)
t.forward(30)

# Ninth letter
t.forward(100)
t.right(100)
t.forward(90)
t.penup()
t.forward(10)
t.left(10)
t.right(90)
t.forward(20)
t.setheading(90)
t.right(120)
t.pendown()
t.circle(20, 110)
t.forward(90)
t.setheading(90)
t.left(90)
t.forward(100)
t.penup()
t.left(90)
t.forward(100)
t.left(100)
t.pendown()
t.circle(100, 10)
t.forward(20)
t.left(40)
t.circle(200, 30)
t.forward(10)

turtle.exitonclick()