from turtle import Turtle
import random

# CONSTANTS -START
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0
MOVE_DISTANCE = 10
# CONSTANTS -END

class Ball(Turtle):

    def __init__(self, scr_h):
        super().__init__()
        self.scr_h = scr_h
        self.x_direction = MOVE_DISTANCE
        self.y_direction = MOVE_DISTANCE
        self.setup()

    def setup(self):
        self.color("white")
        self.shape("square")
        self.penup()
        self.serve(self.scr_h)

    def bounce_y(self):
        self.y_direction *= -1

    def bounce_x(self):
        self.x_direction *= -1

    def serve(self, scr_h):
        self.goto(0, random.randrange(int((-scr_h/2+100)/10)*10, int((scr_h/2-100)/10)*10, 10))
        self.move()

    def move(self):
        self.goto(self.xcor() + self.x_direction, self.ycor() + self.y_direction)



