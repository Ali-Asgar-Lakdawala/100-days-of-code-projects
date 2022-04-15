from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    

    def __init__(self,location_x,location_y):
        super().__init__()
        self.color(random.choice(COLORS))
        self.start_pos_car_x=random.randrange(location_x[0],location_x[1],20)
        self.start_pos_car_y=random.randrange(location_y[0],location_y[1],20)
        self.penup()
        self.shape('square')
        self.goto(self.start_pos_car_x,self.start_pos_car_y)

    
    def car_move(self):
        self.backward(STARTING_MOVE_DISTANCE)
    




        
        

