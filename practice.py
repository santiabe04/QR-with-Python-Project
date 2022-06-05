from tkinter import *

class Practice():
    def __init__(self) -> None:
        self.root = Tk()

    def login_screen(self,buttonState):
        '''TEST -- Writes in login screen'''
        labelLogIn = Label(self.root, text = "Log In").pack()
        self.entryUsername = Entry(self.root) #, bg = "#d7cac7", fg = "#000000"
        labelUsername = Label(self.root, text = "Username").pack()

        myButton = Button(self.root, text = "Log In", state = buttonState, command = self.button_click(), bg = "#d7cac7")
        myButton.pack()

        self.root.mainloop() #Runs the main loop from tkinter

    def button_click(self):
        '''When a button is pressed it's triggered'''
        print("Button Clicked")
        print(self.entryUsername.get())