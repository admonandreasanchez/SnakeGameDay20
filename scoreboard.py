
from turtle import Turtle

INITIAL_SCORE = 0
ALIGNMENT = 'center'
FONT = ('Arial', 16, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.color('white')
        self.speed("fastest")
        self.goto(-10, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", True, align=ALIGNMENT,font=FONT)

    def reset(self):
        self.goto(-10, 270)
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self, score_increment):
        self.score += score_increment
        self.clear()
        self.penup()
        self.color('white')
        self.speed("fastest")
        self.goto(-10, 270)
        self.update_scoreboard()

    def draw_permanent_border(self):
        border = Turtle()
        border.penup()
        border.color('white')
        border.speed("fastest")
        border.goto(-300, 300)
        border.pendown()
        for _ in range(4):
            border.forward(600)
            border.right(90)
        border.hideturtle()
















