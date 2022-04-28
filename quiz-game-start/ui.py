
from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class user_interface():
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain

        
        self.window=Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)

        self.canvas=Canvas(width=300,height=250,highlightthickness=0,bg='white')
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)

        
        self.question_text=self.canvas.create_text(150,125,text='some text',width=250)

        self.get_next_question()
        self.score_text=Label(text=f'score: {self.quiz.score}/{self.quiz.question_number}',bg=THEME_COLOR,fg='white')
        self.score_text.grid(column=1,row=0)

        wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_image,highlightthickness=0,command=self.is_false)
        self.wrong_button.grid(row=2, column=0)

        right_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_image,highlightthickness=0,command=self.is_true)
        self.right_button.grid(row=2, column=1)
        
        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            question=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question)
        else:
            self.canvas.itemconfig(self.question_text, text='This is the end of the quiz')
            self.right_button.config(state='disabled')
            self.wrong_button.config(state='disabled')
        

    def is_true(self):
        is_correct=self.quiz.check_answer('True')
        self.score_text.config(text=f'score: {self.quiz.score}/{self.quiz.question_number}')
        self.fedback(is_correct)

    def is_false(self):
        is_correct=self.quiz.check_answer('False')
        self.fedback(is_correct)

    def fedback(self,is_correct):

        if is_correct:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
            
        self.window.after(1000,self.get_next_question)


        









