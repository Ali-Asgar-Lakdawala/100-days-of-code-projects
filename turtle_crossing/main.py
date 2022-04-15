import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


CARS=[]
count=5

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True

player=Player()
screen.onkeypress(player.move,'Up')
screen.listen()

scoreboard=Scoreboard()

# on screen car location range
location_x=(-50,280)
location_y=(-250,250)

# add new cars on the screen
for i in range(6):
    car=CarManager(location_x,location_y)
    CARS.append(car)

#oringin car location range
location_x=(280,300)
location_y=(-250,250)

while game_is_on:
    time.sleep(0.1)

    for i in CARS:
        i.car_move()

        # game over
        if player.distance(i)<20:
            scoreboard.game_over()
            game_is_on=False

        # remove the cars which are no longer on the screen
        if i.xcor()<-300:
            CARS.remove(i)
            i.hideturtle()
       
        
    #to reduce the car creation
    if count%5==0:
        car=CarManager(location_x,location_y)
        CARS.append(car)

    # refrest the score when turtle reaches the top
    if player.ycor()>280:
        scoreboard.refrest_score()
        player.reset_to_origin()
    
    count+=1

    screen.update()

screen.exitonclick()