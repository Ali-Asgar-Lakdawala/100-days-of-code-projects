from turtle import Turtle,Screen,position
from snake import Snake

screen=Screen()
screen.setup(600,600)
screen.bgcolor('black')

snake_segments=[]
starting_pos=[(0,0),(-20,0),(-40,0)]
screen.tracer(0)
for pos in starting_pos:
    segment=Turtle(shape='square')
    segment.color('white')
    segment.penup()
    segment.goto(pos)
    snake_segments.append(segment)
screen.update()


snake=Snake(snake_segments,screen)
snake.move_snake()