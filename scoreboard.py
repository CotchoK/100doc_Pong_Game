from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.p1_points = 0
        self.p2_points = 0
        self.setup()

    def setup(self):
        self.penup()
        self.hideturtle()
        self.pencolor("white")
        self.goto(0, 250)
        self.display_score()

    def update_score(self, player):
        if player == 1:
            self.p1_points += 1
            self.display_score()
        elif player == 2:
            self.p2_points += 1
            self.display_score()

    def display_score(self):
        self.clear()
        self.write(arg=f"{self.p1_points}          {self.p2_points}",
                   align="center",
                   font=('Courier', 40, 'normal'))



