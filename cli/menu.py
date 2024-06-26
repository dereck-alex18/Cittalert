import sys
from cli.authentication import UserManager
from utils.clear_screen import clear_screen

class CLIMenu:

    def __init__(self):
        self.user_manager = UserManager()

    def welcome_message(self):
        clear_screen("Loading login screen...")
        print('*' * 20)
        print("Welcome to Cittalert! Please, choose an option to continue")
        print('*' * 20)

    def bye_message(self):
        print('*' * 20)
        print("Thank you for using Cittalert! We hope you will come back soon!")
        print('*' * 20)
       
    def initial_menu(self):
        print('[1] Login\n[2] Sign up\n[0] Exit')
        
        try:
            option = int(input())
            self.choose_login_signup(option)
        except ValueError:
            print("Invalid option. Please try again.")
            self.initial_menu()
        

    def choose_login_signup(self, option):
        if option == 1:
           print('Enter the Username')
           username = input()
           print('Enter the Password')
           password = input() 

           loggedInUser = self.user_manager.login_user(username, password)

           clear_screen("Verifing user credencials...")

           if loggedInUser:
                from cli.user_menu import UserMenu
                self.user_menu = UserMenu()
                
                print("Login successful!")
                print("Welcome back, " + loggedInUser["username"])
                self.user_menu.user_menu(loggedInUser)
           else:
                
                print("Login failed. Incorrect username or password!")
                self.initial_menu()    
        
        elif option == 2:
            print('Enter the Username')
            username = input()
            print('Enter the Password')
            password = input() 

            createdUser = self.user_manager.save_user_data(username, password)

            clear_screen("Signing up...")
            if createdUser:
                print("Sign up successful. Now you can login with your new account!")
                
            else:
                print("Username already taken. Please take another username and try again!")
            self.initial_menu()
        
        elif option == 0:
            self.bye_message()
            sys.exit(0)
            
        else:
            print("Invalid option. Please try again.")
            self.initial_menu()

      

