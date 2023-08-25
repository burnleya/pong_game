from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


player_one = Paddle()
player_two = Paddle()
ball = Ball()
score = Score()
screen.listen()
screen.onkey(player_one.move_up, "q")
screen.onkey(player_one.move_down, "a")
screen.onkey(player_two.move_up, "Up")
screen.onkey(player_two.move_down, "Down")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(player_one) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    if ball.distance(player_two) < 50 and ball.xcor() > 340:
        ball.bounce_x()

    if ball.xcor() > 450:
        ball.reset()
        score.player_one()

    if ball.xcor() < -450:
        ball.reset()
        score.player_two()


screen.exitonclick()

if __name__ == '__main__':
    pass


