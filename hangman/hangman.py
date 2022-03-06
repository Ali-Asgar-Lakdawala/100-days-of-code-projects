import hangman_art
import hangman_words
import random

words = hangman_words.word_list
stages = hangman_art.stages_of_hangman
logo=hangman_art.logo

print(logo)
random_word=random.choice(words)
print(random_word)
random_word_list=[]

#to create the list of ___ char 
for i in range(len(random_word)):
    random_word_list.append("_")
print(f"The word is {''.join(random_word_list)} ")

life=7
wrong_alphabet=[]
while random_word_list.count("_")>0:
    user_input=input('guess a word: ').lower()
    if user_input in wrong_alphabet:
        print("this alphabet was marked as wrong try again")
        continue
    if user_input in random_word:
        for i,v in enumerate(random_word):
            if v==user_input:
                random_word_list[i]=v
    else:
        print(stages[life-1])
        wrong_alphabet.append(user_input)
        life-=1

    print(f"The word is {''.join(random_word_list)} ")
    
    if random_word_list.count("_")==0:
        print("You Won")
    if life==0:
        print('You Loose')
        break