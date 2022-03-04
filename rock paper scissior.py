import random
trials_num=int(input('how many times you want to play'))
trials_count=0
user_pt=0
computer_pt=0
def choice(integer):
    if integer==1:
        return 'rock'
    elif integer==2:
        return 'papper'
    else:
        return 'scissor'
def print1():
    print(f'computer choice {computer_choice}, your choice {user_choice}')
while trials_count<trials_num:
    computer_choice=choice(random.randint(1,3))
    user_choice=choice(input('for rock press 1\nfor papper press 2\nfor scissor press 3\n'))

    if user_choice=='rock' and computer_choice=='papper':
        print('computer wins')
        computer_pt+=1
        print1()
    elif user_choice=='papper' and computer_choice=='rock':
        print('user wins')
        print1()
        user_pt+=1

    elif user_choice=='rock' and computer_choice=='scissor':
        print('user wins')
        print1()
        user_pt+=1
    elif user_choice=='scissor' and computer_choice=='rock':
        print('computer wins')
        print1()
        computer_pt+=1

    elif user_choice=='papper' and computer_choice=='scissor':
        print('computer wins')
        print1()
        computer_pt+=1
    elif user_choice=='scissor' and computer_choice=='papper':
        print('user wins')
        print1()
        user_pt+=1
    else:
        print(f'tie')
        print1()
        trials_count-=1
    
    trials_count+=1

if computer_pt>user_pt:
    print(f"final will by computer computer points: {computer_pt} user points: {user_pt}")
else:
    print(f"final will by user computer points: {computer_pt} user points: {user_pt}")

