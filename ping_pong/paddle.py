from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,paddle_position):
        super().__init__()
        self.paddle_position=paddle_position
        self.penup()
        self.color('white')
        self.shape('square')
        self.speed(0)
        self.goto(self.paddle_position)
        self.turtlesize(stretch_wid=5,stretch_len=1)
    
    def upward(self):
        position=list(self.pos())
        position[1]+=20
        self.goto(position)

    def downward(self):
        position=list(self.pos())
        position[1]-=20
        self.goto(position)