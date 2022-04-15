from turtle import Turtle
import time
steps=20



class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_value=steps
        self.y_value=steps
        
    def move_ball(self):
        time.sleep(0.1)
        x_pos=self.xcor()+self.x_value
        y_pos=self.ycor()+self.y_value
        self.goto(x_pos,y_pos)

    def bounce_wall(self):
        self.y_value=self.y_value*(-1) 

    def bounce_paddle(self):
        self.x_value=self.x_value*(-1)  

    def reset_position(self):
        self.goto(0,0)
        self.x_value=self.x_value*(-1)
        self.y_value=self.y_value*(-1)


    
        