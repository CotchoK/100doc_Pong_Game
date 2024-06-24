from turtle import Turtle, Screen

# create screen
scr = Screen()
# create line
line = Turtle()

# screen attributes
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 550
SCREEN_COLOUR = "black"
scr.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
scr.colormode(255)
scr.bgcolor(SCREEN_COLOUR)

#line attributes
line.setpos(x=0, y=int(SCREEN_HEIGHT/2))
line.hideturtle()
line.shapesize(10)
line.setheading(270)
line.pencolor("white")
line.pensize(4)
line.speed("fastest")

# draw line on screen
while line.ycor() > int(-SCREEN_HEIGHT/2):
    line.pendown()
    line.forward(10)
    line.penup()
    line.forward(20)

# prevent premature closing of screen
scr.exitonclick()
