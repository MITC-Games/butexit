from tkinter import *

window = Tk()

window.title("ButExit-Rewritten (beta)")

window.geometry('512x512')

def clicked():

    exit()

photo = PhotoImage(file = r"./boton.png")

btn = Button(window, text="Click Me", command=clicked, image=photo)

btn.grid(column=1, row=0)

window.mainloop()