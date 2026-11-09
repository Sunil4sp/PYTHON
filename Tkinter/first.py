from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("My First GUI")
window.geometry('400x400')

#icon = PhotoImage(file="profile.png")
#window.iconphoto(True, icon)
Label(window, text="Hello, Tkinter!").pack()

window.mainloop()


