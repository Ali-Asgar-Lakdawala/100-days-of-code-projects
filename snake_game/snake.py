from turtle import Turtle
starting_pos=[(0,0),(-20,0),(-40,0),(-60,0),(-80,0),(-100,0),(-120,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
MOVE_DIST=20

class Snake:


    def __init__(self,screen):
        self.snake_segments = []
        self.screen=screen
        self.create_snake()
        self.head = self.snake_segments[0]
        

    def move_snake(self):
        for i in range(len(self.snake_segments)-1,0,-1):
            self.snake_segments[i].goto(self.snake_segments[i-1].position())

        self.snake_segments[0].forward(MOVE_DIST)


    def create_snake(self):
        for pos in starting_pos:
            segment=Turtle(shape='square')
            segment.color('white')
            segment.penup()
            segment.goto(pos)
            self.snake_segments.append(segment)

    def snake_ate_food(self):
        segment=Turtle(shape='square')
        segment.color('white')
        segment.penup()
        segment.goto(self.snake_segments[-1].position())
        self.snake_segments.append(segment)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)