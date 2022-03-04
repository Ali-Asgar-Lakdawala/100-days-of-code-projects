print('welcome')
character_cnt=int(input('how many letters would you like in your password'))
symbols_cnt=int(input("how many symbols would you like"))
numbers_cnt=int(input('how many numbers would you like'))
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


import random
random_numbers=random.randrange(0,10)
output=[]
for i in range(numbers_cnt):
    output.append(str(random.randrange(0,10)))

for i in range(symbols_cnt):
    output.append(random.choice(symbols))

for i in range(character_cnt):
    output.append(random.choice(letters))

random.shuffle(output)
print("".join(output))