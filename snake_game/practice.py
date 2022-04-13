from turtle import Screen, Turtle
import random
import secrets
ali_turtle=Turtle()
screen=Screen()

def m_forward():
    ali_turtle.forward(10)
def m_backward():
    ali_turtle.backward(10)
def m_right():
    ali_turtle.right(5)
def m_left():
    ali_turtle.left(5)
def clean():
    ali_turtle.clear()
    ali_turtle.penup()
    ali_turtle.home()
    ali_turtle.pendown()

screen.onkeypress(m_forward,'w')
screen.onkeypress(m_backward,'s')
screen.onkeypress(m_right,'d')
screen.onkeypress(m_left,'a')
screen.onkeypress(clean,'c')
screen.listen()

screen.exitonclick()
