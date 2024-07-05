from turtle import Turtle, Screen
import paddle
import ball
import time

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
player_1 = paddle.Paddle(PLAYER_XCOR, 0)
player_2 = paddle.Paddle(COMPUTER_XCOR, 0)
ball = ball.Ball(SCREEN_HEIGHT)

# player controls
scr.onkey(player_1.move_up, "w")
scr.onkey(player_1.move_down, "s")
scr.onkey(player_2.move_up, "Up")
scr.onkey(player_2.move_down, "Down")

game_over = False

while not game_over:
    time.sleep(0.07)
    scr.update()

    if ball.distance(ball.xcor(), SCREEN_HEIGHT/2 - 10) < 10 or ball.distance(ball.xcor(), -SCREEN_HEIGHT/2 + 10) < 15:
        ball.bounce_y()
    elif ball.xcor() + 10 > player_2.xcor():
        print("point player 1")
        ball.bounce_x()
        ball.serve(SCREEN_HEIGHT)
    elif ball.xcor() - 10 < player_1.xcor():
        print("point player 2")
        ball.bounce_x()
        ball.serve(SCREEN_HEIGHT)
    elif ball.xcor() + 10 == player_2.xcor() - 10 \
            and ball.ycor() + 10 > player_2.ycor() - 50 \
            and ball.ycor() - 10 < player_2.ycor() + 50 \
            or ball.xcor() - 10 == player_1.xcor() + 10 \
            and ball.ycor() + 10 > player_1.ycor() - 50 \
            and ball.ycor() - 10 < player_1.ycor() + 50 :
        ball.bounce_x()

    ball.move()


    print(f"{ball.xcor()}, {ball.ycor()}: | {SCREEN_HEIGHT/2 -30}")
# prevent premature closing of screen
scr.exitonclick()


