import pandas as pd
from turtle import Screen, Turtle

correct_ans=[]

df=pd.read_csv('50_states.csv')

screen = Screen()
screen.title('US States game')
image='blank_states_img.gif'
screen.addshape(image)
game=Turtle()
game.shape(image)




while True:


    text=screen.textinput(title=f'Score {len(correct_ans)} / 50 states',prompt='whats the states name')
    text=text.capitalize()

    if text== 'Exit':
        break


    if text in df['state'].to_list() and text not in correct_ans:
        correct_ans.append(text)

        state=Turtle()
        state.penup()
        state.hideturtle()

        x_cord=df[df['state']==text].x.values[0]
        y_cord=df[df['state']==text].y.values[0]

        state.goto(x_cord,y_cord)
        state.write(text)


states_to_learn=df.set_index('state').drop(correct_ans,axis=0)
states_to_learn.to_csv('states_to_learn.csv')