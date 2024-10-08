
from turtle import  Turtle
import time

STARTING_POSITIONS =  [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]

    def create_snake(self):
        for position  in STARTING_POSITIONS:
            self.add_square(position)

    def add_square(self, position):
        new_sqr = Turtle(shape="square")
        new_sqr.color('white')
        new_sqr.penup()
        new_sqr.goto(position)
        self.squares.append(new_sqr)

    def extend(self):
        #add a new square to the snake
        self.add_square(self.squares[-1].position())


    def move(self):
        for sqr_nr in range(len(self.squares)-1,0,-1):
            new_x = self.squares[sqr_nr -1 ].xcor()
            new_y = self.squares[sqr_nr - 1].ycor()
            self.squares[sqr_nr].goto(new_x,new_y)
        self.squares[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)