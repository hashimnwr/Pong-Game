from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.score_paddle_1 = 0
        self.score_paddle_2 = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(x=100, y=200)
        self.write(self.score_paddle_1, align='center', font=('Courier', 80, 'normal'))
        self.goto(x=-100, y=200)
        self.write(self.score_paddle_2, align='center', font=('Courier', 80, 'normal'))

    def p1_point_up(self):
        self.score_paddle_1 +=1
        self.update_scoreboard()

    def p2_point_up(self):
        self.score_paddle_2 += 1
        self.update_scoreboard()