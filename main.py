from turtle import Screen
from paddle import Paddle
from balls import Ball
from time import sleep
from scoreboard import Score


screen = Screen()
ball = Ball()
points = Score()

screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))


screen.listen()
screen.onkey(paddle1.go_up, 'Up')
screen.onkey(paddle1.go_down, 'Down')
screen.onkey(paddle2.go_up, 'w')
screen.onkey(paddle2.go_down, 's')

game_on = True
while game_on:
    sleep(ball.movement_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.vertical_bounce()

    if ball.distance(paddle1) < 55 and ball.xcor() > 325 or ball.distance(paddle2) < 55 and ball.xcor() < -325:
        ball.horizontal_bounce()

    if ball. xcor() > 380:
        #paddle2 scores
        points.p2_point_up()
        ball.reset_position()
    if ball.xcor() < -380:
        #paddle1 scores
        points.p1_point_up()
        ball.reset_position()


screen.exitonclick()
