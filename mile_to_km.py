import tkinter

window=tkinter.Tk()
window.title('Mile To KM')
window.minsize(width=200,height=200)


text1=tkinter.Label(text='is equal to')
text1.grid(column=0,row=1)

input_miles=tkinter.Entry(width=10)
input_miles.grid(column=1,row=0)

text2=tkinter.Label(text='Miles')
text2.grid(column=2,row=0)

text3=tkinter.Label(text='KM')
text3.grid(column=2,row=1)

def change_text():
    output=int(input_miles.get())*1.60934
    output_1.config(text=output)

buttion1=tkinter.Button(text='convert',command=change_text)
buttion1.grid(column=1,row=2)

output_1=tkinter.Label()
output_1.grid(column=1,row=1)




window.mainloop()