from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()

screen.setup(width=800, height=600)
screen.title("Arcade Pong")
screen.bgcolor("black")
screen.tracer(0)

LEFT_END = (-350, 0)
RIGHT_END = (350, 0)

paddle_r = Paddle(RIGHT_END)
paddle_l = Paddle(LEFT_END)
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(paddle_r.move_up,"Up")
screen.onkey(paddle_r.move_down,"Down")

screen.onkey(paddle_l.move_up,"w")
screen.onkey(paddle_l.move_down, "s")


game_over = False

while not game_over:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()

    # detecting collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        # ball bounces
        ball.bounce_y()

    # collision with paddles
    if ball.distance(paddle_l)<50 and ball.xcor()< -320 or ball.distance(paddle_r)<50 and ball.xcor()>320:
        ball.bounce_x()

    # missed by paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()