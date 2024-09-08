import turtle
from turtle import Turtle, Screen
from random import randint, choice

timmy = Turtle()
timmy.shape('arrow')
screen = Screen()
'''for i in range(4):
    timmy.forward(100)
    timmy.right(90)
'''

#Draw a dashed line
"""timmy.penup()
timmy.goto(-180,0)
for i in range(15):
    timmy.pendown()
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
"""
#draw polygons
timmy.penup()
#timmy.goto(-100.0, 200.0)
timmy.pendown()
#screen.colormode(255)
turtle.colormode(255)
sides = 3

"""def draw_shape(sides):
    angle = 360 / sides
    for i in range(sides):
        timmy.forward(100)
        timmy.right(angle)

for side_number in range(3, 11):
    r,g,b = (randint(0,255),randint(0,255),randint(0,255))
    timmy.pencolor((r,g,b))
    draw_shape(side_number)"""

"""
# random walk
angles = [0,90,180, 270]
def walk(angle):
    timmy.pensize(6)
    timmy.pencolor((randint(0, 255), randint(0, 255), randint(0, 255)))
    timmy.forward(30)
    timmy.setheading(angle)

for _ in range(200):
    timmy.speed(0)
    walk(choice(angles))
"""
def draw_spirograph(gap_size):
    timmy.pensize(5)
    timmy.speed('fastest')
    for _ in range(360//gap_size):
        
        timmy.pencolor((randint(0,255),randint(0,255),randint(0,255)))
        timmy.circle(100)
        timmy.left(6)

draw_spirograph(5)




screen.exitonclick()