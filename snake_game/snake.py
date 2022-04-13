
import time
from turtle import Turtle,Screen
class Snake:


    def __init__(self,snake_segments,screen):
        self.snake_segments=snake_segments
        self.screen=screen
    
 
    def move_snake(self):

        alive=True
        while alive:
            time.sleep(0.1)

            for i in range(len(self.snake_segments)-1,0,-1):
                self.snake_segments[i].goto(self.snake_segments[i-1].position())

            self.snake_segments[0].forward(10)

            def m_right():
                self.snake_segments[0].right(90)
            def m_left():
                self.snake_segments[0].left(90)
                
            self.screen.onkeypress(m_right,'d')
            self.screen.onkeypress(m_left,'a')
            self.screen.listen()
            self.screen.update()

        self.screen.exitonclick()