from tkinter import *
from tkinter import messagebox
import random
import json


# ---------------------------- check for data exist ------------------------------- #
def exists():
    website = website_entry.get()

    if len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please enter any website name to find its data.")
    else:
        with open('data.json',"r") as txt:
            data=json.load(txt)

        for i,v in data.items():
            if website==i:
                email=v['email']
                password=v['password']
                messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
            else:
                messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
    
    

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for char in range(nr_letters)]
    password_symbol = [random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]
    password_list=password_letter+password_symbol+password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0,END)
    password_entry.insert(0, password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data={
        website:{
            'email':email,
            'password':password
        }
    }
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                      f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            try:
                with open('data.json',"r") as data_json:
                    #reading old data
                    data=json.load(data_json)
                    #updating the old data
                    data.update(new_data)
            except:
                with open('data.json',"w") as data_json:
                    json.dump(new_data,data_json,indent=4)

                    website_entry.delete(0,END)
                    password_entry.delete(0,END)
            else:
                #wring the new data in file     
                with open('data.json',"w") as data_json:
                    json.dump(data,data_json,indent=4)

                    website_entry.delete(0,END)
                    password_entry.delete(0,END)
                
            

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=25, justify='left')
website_entry.grid(row=1, column=1)
email_entry = Entry(width=45, justify='left')
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "aliasgarlakdawala0209@gmail.com")
password_entry = Entry(width=25, justify='left')
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", width=15,command=password_generator)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=34,command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button=Button(text="Search", width=15,command=exists)
search_button.grid(row=1, column=2)

window.mainloop()