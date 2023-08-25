from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.penup()
        self.hideturtle()
        self.player_one_score = 0
        self.player_two_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.player_one_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.player_two_score, align="center", font=("Courier", 80, "normal"))

    def player_one(self):
        self.player_one_score += 1
        self.update_scoreboard()

    def player_two(self):
        self.player_two_score += 1
        self.update_scoreboard()
