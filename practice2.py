from tkinter import *

root = Tk()

e = Entry(root)

def button_click():
    '''When a button is pressed it's triggered'''
    print("Button Clicked")
    print(e.get())

myButton = Button(root, text = "Log In", state = "active", command = button_click(), bg = "#d7cac7")
myButton.pack()

root.mainloop() #Runs the main loop from tkinter