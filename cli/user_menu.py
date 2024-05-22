import os
from cli.authentication import UserManager

class UserMenu():

    def __init__(self):
        self.user_manager = UserManager()

    def user_menu(self, loggedin_user):
        print('''
              [1] Visualize all Alerts
              [2] Create Alerts
              [3] Update Alerts
              [4] Delete Alerts
              [5] Ombudsman
              [6] My Account
              [7] Logout
              ''')
        
        option = int(input('Choose one of the options above\n'))
        self.user_options(option, loggedin_user)

    def user_options(self, option, loggedin_user):
        match option:
            case 1:
                print("Visualize all Alerts")
            case 2:
                print("Create Alerts")
            case 3:
                print("Update Alerts")
            case 4:
                print("Delete Alerts")
            case 5:
                print("Ombudsman")
            case 6:
                from cli.account_settings import UserAccount
                self.account_settings = UserAccount()
                self.account_settings.change_user_account(option, loggedin_user)
            case 7:
                self.logout()
    
    def logout(self):
        from cli.menu import CLIMenu
        self.initial_menu = CLIMenu()
        loggedInUser = None
        self.initial_menu.welcome_message()
        self.initial_menu.initial_menu()
                
