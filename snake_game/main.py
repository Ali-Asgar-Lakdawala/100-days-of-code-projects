from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.title("My Snake Game")

screen.tracer(0)

food=Food()
snake=Snake(screen)
scorecard=Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

alive=True
while alive:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    #snake eating the food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.snake_ate_food()
        scorecard.update_score()

    #snake coliding with wall
    if snake.head.position()[0]>280 or snake.head.position()[0]<-280 or snake.head.position()[1]>280 or snake.head.position()[1]<-280 :
        alive=False
        scorecard.game_over()

    #snake coliding with itself
    for snake_segment in snake.snake_segments[1:]:
        if snake.head.distance(snake_segment)<15:
            alive=False
            scorecard.game_over()

screen.exitonclick()