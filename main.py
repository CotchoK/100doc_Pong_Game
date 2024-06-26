from turtle import Turtle, Screen
import paddle

# SCREEN (START)
# screen constants
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
SCREEN_COLOUR = "black"
SCREEN_TITLE = "Pong Game"
scr = Screen()

# screen setup
scr.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
scr.colormode(255)
scr.bgcolor(SCREEN_COLOUR)
scr.title(SCREEN_TITLE)
scr.tracer(0)
scr.listen()


def paint_line():
    # DRAW MID SCREEN LINE - FOR DELINEATING EACH PLAYERS' HALF
    # create line
    line = Turtle()
    # line attributes
    line.penup()
    line.hideturtle()
    line.shapesize(10)
    line.pencolor("white")
    line.pensize(4)
    line.speed("fastest")
    line.goto(x=0, y=int(SCREEN_HEIGHT / 2))
    line.setheading(270)

    # draw line on screen
    while line.ycor() > int(-SCREEN_HEIGHT / 2):
        line.pendown()
        line.forward(10)
        line.penup()
        line.forward(20)

# paddle constants
PLAYER_XCOR = int(-SCREEN_WIDTH/2) + 40
COMPUTER_XCOR = int(SCREEN_WIDTH/2) - 40

paint_line()

# set up player
player = paddle.Paddle(PLAYER_XCOR, 0)
computer = paddle.Paddle(COMPUTER_XCOR, 0)

# player controls
scr.onkey(player.move_up, "Up")
scr.onkey(player.move_down, "Down")

game_over = False

while not game_over:
    scr.update()

# prevent premature closing of screen
scr.exitonclick()


