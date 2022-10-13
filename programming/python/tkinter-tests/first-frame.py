from tkinter import *
from os import system
from time import sleep

def function():
    fl_lable = Label(root,text="FischLord war hier").pack()

root =Tk()

#widgets
mybutton = Button(root,text="Okay",padx=50,pady=50,command=function).pack()


#placing


root.mainloop()


sleep(2)
system("cls")