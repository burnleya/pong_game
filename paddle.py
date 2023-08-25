from turtle import Turtle


class Paddle(Turtle):

    player_num = 0

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        Paddle.player_num += 1
        self.set_position()
        self.y_position = 0

    def set_position(self):
        if Paddle.player_num == 1:
            self.goto(-390, 0)
        else:
            self.goto(380, 0)

    def move_up(self):
        self.sety(self.y_position)
        self.y_position += 20

    def move_down(self):
        self.sety(self.y_position)
        self.y_position -= 20














