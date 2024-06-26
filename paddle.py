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
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.goto(x_pos, y_pos)
        self.setheading(UP)

    def move_up(self):
        self.setheading(UP)
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.setheading(DOWN)
        self.forward(MOVE_DISTANCE)

