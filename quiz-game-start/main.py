from data import question_data
from question_model import question_ans
from quiz_brain import quiz
q_a_list=[]

for q in question_data:
  q_text=q['text']
  a_text=q['answer']
  new_question=question_ans(q_text,a_text)
  q_a_list.append(new_question)

aliasgar=quiz(q_a_list,0)

while aliasgar.still_has_questions():
    aliasgar.next_question()
    

