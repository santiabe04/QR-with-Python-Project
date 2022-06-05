'''View Code -- Santiago Abelle'''
from tkinter import * #Import graphic UI library

class View():
    def __init__(self):
        '''Is the initiation from the class'''
        self.root = Tk() #Creates a new tkinter object
    
    # def write_screen(self,messageList,buttonState):
    #     '''Writes in screen'''
    #     j = 0
    #     entries = []
    #     for i in messageList: #For every tuple in the list
    #         myLabel = Label(self.root, text = i[1]).grid(row = j, column = i[0]) #Label(tkinter_object, text = message_list[message]) and grid(row = auto_incrementable, column = message_list[tree_number])
    #         if(i[1] != "Log In"):
    #             myEntry = Entry(self.root, bg = "#d7cac7", fg = "#000000").grid(row = j, column = i[0] + 1)
    #             entries.append(myEntry.get())
    #         j += 1

    #     myButton = Button(self.root, text = "Log In", state = buttonState, command = self.button_click(entries), bg = "#d7cac7") #Button(tkinter_object, text, state = buttonState, command = trigger_function)
    #     myButton.grid()

    #     self.root.mainloop() #Runs the main loop from tkinter

    def login_screen(self,buttonState):
        '''TEST -- Writes in login screen'''
        labelLogIn = Label(self.root, text = "Log In").grid(row = 0, column = 0)
        entryUsername = Entry(self.root, bg = "#d7cac7", fg = "#000000").grid(row = 1, column = 2)
        labelUsername = Label(self.root, text = "Username" + entryUsername.get()).grid(row = 1, column = 1)
        entryPassword = Entry(self.root, bg = "#d7cac7", fg = "#000000").grid(row = 2, column = 2)
        labelPassword = Label(self.root, text = "Password" + entryPassword.get()).grid(row = 2, column = 1)

        entries = [entryUsername.get(), entryPassword.get()]

        myButton = Button(self.root, text = "Log In", state = buttonState, command = self.button_click(entries), bg = "#d7cac7")
        myButton.grid()

        self.root.mainloop() #Runs the main loop from tkinter

    def button_click(self, entries):
        '''When a button is pressed it's triggered'''
        print("Button Clicked")
        print(entries[0])
        print(entries[1])