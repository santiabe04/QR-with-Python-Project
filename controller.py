'''Controller Code -- Santiago Abelle'''
from model import Model #Import the Model class
from view import View #Import the View class
from practice import Practice #ONLY FOR TESTING -- Import the Practice class
from qr_encode import Encode #Import the Encode class
from qr_decode import Decode #Import the Decode class

class Controller():
    def __init__(self):
        '''Is the initiation from the class'''
        #self.Practice = Practice() #Creates a new Practice object
        self.View = View() #Creates a new View object
        self.Model = Model() #Creates a new Model object
        self.Encode = Encode() #Creates a new Encode object
        self.Decode = Decode() #Creates a new Decode object
        self.main() #Runs the main function

    def main(self):
        '''Is the main loop'''
        buttonState = "normal"
        while True:
            messageList = [[0,'Log In'],[1,'Username'],[1,'Password']] #TEST -- Messages to print in screen with the row
            self.View.login_screen(buttonState) #Calls write_screen from View class
            #self.Practice.login_screen(buttonState) #Calls write_screen from Practice class
            test = input('') #TEST -- Is to prevent from closing the program

if __name__ == "__main__":
    controller = Controller()