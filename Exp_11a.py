import tkinter

window = tkinter.Tk()
window.title("GUI")

def say_hi():
	tkinter.Label(window, text = "Hi! Welcome to python programming").pack()

tkinter.Button(window, text = "Click Me!", command = say_hi).pack()

window.mainloop()

