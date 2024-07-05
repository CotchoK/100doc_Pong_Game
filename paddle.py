from turtle import Turtle

# CONSTANTS -START
UP = 90
DOWN = 270
MOVE_DISTANCE = 20
# CONSTANTS -END

class Paddle(Turtle):

    def __init__(self, x_coord, y_coord):
        super().__init__()
        # setup settings for paddle
        self.setup(x_coord, y_coord)

    def setup(self, x_pos, y_pos):
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x_pos, y_pos)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)

