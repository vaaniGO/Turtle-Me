import turtle
import math
t = turtle.Turtle()
t.speed(0)
t.pensize(2)

def trisect(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    p1_3 = ((2*x1 + x2)/3, (2*y1 + y2)/3) 
    p2_3 = ((x1 + 2*x2)/3, (y1 + 2*y2)/3) 
    return p1_3, p2_3

def thirdVertex(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    xm, ym = ((x1 + x2) / 2, (y1 + y2) / 2)  
    theta = math.radians(60)  
    x3 = xm + (y2 - y1) * math.sqrt(3) / 2
    y3 = ym - (x2 - x1) * math.sqrt(3) / 2
    return (x3, y3)

# Principle: Every trisection gives us 4 new sides, each of which are then trisected again
def kochSegment(p1, p2, level):
    if level == 0:
        t.penup()
        t.goto(p1)
        t.pendown()
        t.goto(p2)
    else:
        # Basically take the two points of trisection and find their 'third vertex' i.e. if those two points were the base of a equilateral triangle what would be their third vertex
        p1_3, p2_3 = trisect(p1, p2)
        p3 = thirdVertex(p1_3, p2_3)
        # We will get 4 new sides to further trisect based on the 'third vertex'.
        kochSegment(p1, p1_3, level - 1)
        kochSegment(p1_3, p3, level - 1)
        kochSegment(p3, p2_3, level - 1)
        kochSegment(p2_3, p2, level - 1)

def kochSnowflake(p1, p2, p3, level):
    kochSegment(p1, p2, level)
    kochSegment(p2, p3, level)
    kochSegment(p3, p1, level)

A = (-150, -50)
B = (150, -50)
C = (0, 150)

kochSnowflake(A, B, C, 4) 

turtle.exitonclick()
