"""import colorgram


rgb_colors = []
colors = colorgram.extract('./hirst.jpg', 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)"""
import turtle
from turtle import Turtle, Screen
import random
from PIL.ImageChops import screen

color_list = [ (221, 232, 225), (208, 160, 82), (55, 89, 132), (145, 91, 40), (139, 26, 48), (222, 207, 105), (132, 176, 203), (45, 55, 104), (158, 46, 84), (169, 159, 40), (128, 189, 143), (84, 20, 44), (38, 43, 66), (187, 93, 106), (188, 138, 167), (84, 123, 182), (59, 39, 30), (79, 153, 165), (88, 157, 90), (195, 80, 71), (159, 201, 220), (79, 74, 43), (45, 74, 77), (59, 127, 118), (218, 176, 187), (167, 207, 165), (179, 188, 212)]

tim = Turtle()
turtle.colormode(255)
tim.penup()
tim.hideturtle()
tim.speed(0)

x = -200
y = -100
tim.setposition(x, y)
step = 30
for _ in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(step)
    y += step
    tim.setposition(x, y)

screen = Screen()
screen.exitonclick()