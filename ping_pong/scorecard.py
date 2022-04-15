from turtle import Turtle

class  Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(0)
        self.Player1score=0
        self.Player2score=0
        self.hideturtle() 
        self.color('white')
        self.refrest_score()
        

    
    def point(self,player):
        self.write("Game over", True, align="center")
        if player==2:
            self.Player1score+=1
            self.refrest_score()
        else:
            self.Player2score+=1
            self.refrest_score()

    def refrest_score(self):
        self.clear()
        self.goto(200,270)
        self.write(f"Player 1 Score = {self.Player1score}", align="center",font=('Arial', 15, 'normal'))
        self.goto(-200,270)
        self.write(f"Player 2 Score = {self.Player2score}", align="center",font=('Arial', 15, 'normal'))

    


