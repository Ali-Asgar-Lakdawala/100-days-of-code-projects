FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('black')
        self.hideturtle()
        self.penup()
        self.goto(-100,250)
        self.score=0
        self.level=1
        self.write(f"Score = {self.score}", align="center",font=FONT)


    
    def refrest_score(self):
        self.clear()
        self.score=self.score+1
        self.write(f"Score = {self.score}", align="center",font=FONT)

    def game_over(self):
        self.goto(100,250)
        self.write(f"game over", align="center",font=FONT)
