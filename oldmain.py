from tkinter import *

window = Tk()

window.title("ButExit-Rewritten (beta)")

window.geometry('200x200')

def clicked():

    exit()

# photo = PhotoImage(file = r"./boton.png") |, image=photo|

btn = Button(window, text="Exit", command=clicked, height=200, width=200).pack()

#btn.grid(column=1, row=0)

window.mainloop()