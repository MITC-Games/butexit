# Import module
from tkinter import *
splash_root = Tk()

def splashscreen():
	
	splash_root.title("ButExit-Rewritten (beta) | Iniciando...")
	# Adjust size
	splash_root.geometry("200x200")

	# Set Label
	splash_label = Label(splash_root,text="Butexit v0.1.1",font=18)
	splash_label.pack()

	# main window function
	

	# Set Interval
	splash_root.after(2000,main)

	# Execute tkinter
	mainloop()

def main():
		# destory splash window
		splash_root.destroy()
		game()
		# Execute tkinter
		#root = Tk()
			
		# Adjust size
		#root.geometry("200x200")
		

def game():
	window = Tk()

	window.title("ButExit-Rewritten (beta)")

	window.geometry('200x200')

	# photo = window.PhotoImage(file = "./boton.png") # |, image=photo|

	btn = Button(window, text="Exit", command=clicked, height=200, width=200).pack()

	#btn.grid(column=1, row=0)


def clicked():

    exit()

splashscreen()
game()


