import os
from cli.authentication import UserManager


class CLIMenu:

    def __init__(self) -> None:
        self.user_manager = UserManager()
    def initial_menu(self):
        print("Welcome to Cittalert! Please, choose an option to continue\n")
        print('[1] Login\n[2] Sign up')
        
        option = int(input())

        if option == 1:
           print('Enter the Username')
           username = input()
           print('Enter the Password')
           password = input() 

           loggedInUser = self.user_manager.login_user(username, password)

           if loggedInUser:
                os.system("clear")
                print("Login successful!!!")
                print("Welcome back, " + loggedInUser["username"])
           else:
                os.system("clear")
                print("Login failed")    
        
        elif option == 2:
            print('Enter the Username')
            username = input()
            print('Enter the Password')
            password = input() 

            createdUser = self.user_manager.save_user_data(username, password)

            if createdUser:
                os.system("clear")
                print("Sign up successful!!!")
            else:
                os.system("clear")
                print("Username already taken!")
            
        else:
            print("Invalid option")
