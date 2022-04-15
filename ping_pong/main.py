from turtle import Screen
from paddle import Paddle
from ball import Ball
from scorecard import Scorecard

screen_height=600
screen_length=800
screen=Screen()
screen.bgcolor('black')

screen.setup(screen_length,screen_height)
screen.title('Ping Pong Game')

scorecard=Scorecard()

paddle1=Paddle(paddle_position=(350,0))
paddle2=Paddle(paddle_position=(-350,0))


screen.onkeypress(paddle1.upward,'Up')
screen.onkeypress(paddle1.downward,'Down')
screen.onkeypress(paddle2.upward,'w')
screen.onkeypress(paddle2.downward,'s')
screen.listen()

ball=Ball()
alive=True
while alive:
    ball.move_ball()

    # collision with the walll
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    #collision with the paddle
    if ball.xcor()>320 or ball.xcor()<-320:
        if ball.distance(paddle1)<60 or ball.distance(paddle2)<60:
            ball.bounce_paddle()
    
    # game over
    if ball.xcor()>340 :
        scorecard.point(1)
        ball.reset_position()
    elif ball.xcor()<-340:
        scorecard.point(2)
        ball.reset_position()
        
        
    
















screen.exitonclick()