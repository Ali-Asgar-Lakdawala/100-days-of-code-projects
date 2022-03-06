alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text,shift,direction):
    output=''
    for i in text:
        if i in alphabet:
            if direction=='encode':
                position=alphabet.index(i)+shift
            else:
                position=alphabet.index(i)-shift
            
            while position>len(alphabet)-1:
                position=position-len(alphabet)

            output+=alphabet[position]
        else:
            output+=i

    print(f"Here's the {direction}d result: {output}")
    restart=input('Type "Yes" if you want to go again, otherwise type "No"').lower()
    while restart=="yes":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(text,shift,direction)
    
    print("Thank you for using this app")


caesar(text,shift,direction)