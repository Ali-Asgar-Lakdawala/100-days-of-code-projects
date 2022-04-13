class quiz:

  def __init__(self,question_bank,question_no):
    self.question_no=question_no
    self.question_bank=question_bank
    self.points=0

  def still_has_questions(self):
    return(self.question_no < len(self.question_bank))

  def next_question (self):
    current_question=self.question_bank[self.question_no]
    self.question_no+=1
    print(f'Q.{self.question_no} {current_question.question} (True/False): ')
    answer=input()
    correct_ans=current_question.answer
    if answer==correct_ans:
        print('your ans is correct')
        self.points+=1
    else:
        print('oops!! wrong ans')
    print(f'The correct ans is {correct_ans}')    
    print(f'{self.points}/{self.question_no} \n')