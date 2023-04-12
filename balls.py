from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        # self.shapesize(stretch_wid=2, stretch_len=2)
        self.goto(x=0, y=0)
        self.xmove = 10
        self.ymove = 10
        self.movement_speed = 0.1

    def move(self):
        newx = self.xcor() + self.xmove
        newy = self.ycor() + self.ymove
        self.goto(x=newx, y=newy)


    def vertical_bounce(self):
        self.ymove *= -1

    def horizontal_bounce(self):
        self.xmove *= -1
        self.movement_speed *= 0.9

    def reset_position(self):
        self.goto(x=0, y=0)
        self.movement_speed = 0.1
        self.horizontal_bounce()