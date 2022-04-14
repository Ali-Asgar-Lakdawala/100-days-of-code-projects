from turtle import Turtle
ALLIGNMENT="center"
FONT=('Arial', 15, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.setposition(0,280)
        self.score=0
        self.clear()
        self.color('white')
        self.hideturtle()
        self.update_score()
        
        
    def update_score(self):
        self.clear()
        self.score+=1
        self.write(f"score ={self.score}", align=ALLIGNMENT,font=FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align=ALLIGNMENT,font=FONT)
