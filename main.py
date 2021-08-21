from tkinter import *

window = Tk()

window.title("ButExit-Rewritten (beta)")

window.geometry('512x512')

def clicked():

    exit()

# photo = PhotoImage(file = r"./boton.png") |, image=photo|

btn = Button(window, text="Exit", command=clicked)

btn.grid(column=1, row=0)

window.mainloop()