from ast import Global
from math import floor
import tkinter
from tkinter.tix import Y_REGION

from isort import file
from regex import R
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS=0
MIN_TO_SEC_MUL=1
TICK=''
TIMER= None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global REPS,TICK,TIMER
    REPS=0
    TICK=''
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text='00:00')
    label_timer.config(text='Timmer',fg=GREEN)
    label_tick.config(text=TICK,fg=GREEN)

def start_again():
    reset()
    start_timer()

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():

    button_start.config(text='start again',command=start_again)
    global REPS
    REPS+=1
    if REPS%8==0:
        count_down(LONG_BREAK_MIN*MIN_TO_SEC_MUL)
        label_timer.config(fg=RED,text='LONG BREAK')
    elif  REPS%2!=0:
        count_down(WORK_MIN*MIN_TO_SEC_MUL)
        label_timer.config(fg=GREEN,text='WORK')
    else:
        count_down(SHORT_BREAK_MIN*MIN_TO_SEC_MUL)
        label_timer.config(fg=PINK,text='SHORT BREAK')
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(sec):
    count_min=floor(sec/60)
    count_sec=sec-count_min*60

    if count_min<10:
        count_min='0'+str(count_min)

    if count_sec<10:
        count_sec='0'+str(count_sec)
    


    #changes the text of the canvas text
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    # update the text after every 1000 ms without forming a loop 
    if sec>0:
        global TIMER
        TIMER=window.after(100,count_down,sec-1)

    if sec==0:
        global TICK
        start_timer()
        if REPS%2==0:
            TICK+='🗸'
            label_tick.config(text=TICK)



# ---------------------------- UI SETUP ------------------------------- #
window=tkinter.Tk()
window.title('pomodoro')
window.config(padx=100,pady=50,bg=YELLOW)

canvas=tkinter.Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
totato_img=tkinter.PhotoImage(file='tomato.png')
canvas.create_image(100,112,image=totato_img)
timer_text=canvas.create_text(100,130,text='00.00',fill='white',font=(FONT_NAME,35,'bold'))
canvas.grid(column=1,row=1)

label_timer=tkinter.Label(text='Timmer',bg=YELLOW,fg=GREEN,font={FONT_NAME,50,'bold'})
label_timer.grid(column=1,row=0)

button_start=tkinter.Button(text='start',width=10,command=start_timer)
button_start.grid(column=0,row=2)

button_reset=tkinter.Button(text='reset',width=10,command=reset)
button_reset.grid(column=2,row=2)

label_tick=tkinter.Label(bg=YELLOW,fg=GREEN,font={FONT_NAME,50,'bold'})
label_tick.grid(column=1,row=3)

window.mainloop()