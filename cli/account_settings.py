import os
from cli.authentication import UserManager

class UserAccount:
    def __init__(self):
        self.user_manager = UserManager()

    def user_account_menu(self):
        print('''
              [1] List all Users
              [2] Change Username
              [3] Change Password
              [4] Delete Account
              [0] Back to User Menu
              ''')
       
    def change_user_account(self, option, loggedin_user):
        from cli.user_menu import UserMenu
        self.user_menu = UserMenu()
        self.user_account_menu()
        option = int(input())
        
        match option:
            case 1:
                all_users = self.user_manager.get_all_usernames()
                print("All Usernames: \n")
             
                for index, user in enumerate(all_users, start=1):
                    print(f"{index} - {user}")
            case 2:
                new_username = input("Please enter your new username\n")
                user = self.user_manager.update_user_username(loggedin_user, new_username)
                if(not user):
                   print("The username is already taken, please choose another one")
                   self.change_user_account(option, loggedin_user)
                else:
                   os.system("clear")
                   print("Username successfully changed")
                   loggedin_user = user
            case 3:
                new_password = input("Please enter your new password\n")
                isChanged = self.user_manager.update_user_password(loggedin_user, new_password)
                if(not isChanged):
                   print("The password is already taken, please choose another one")
                   self.change_user_account(option, loggedin_user)
                else:
                   os.system("clear")
                   print("Password successfully changed")
            case 4:
                user_password = input("Please enter your password to delete your account\n");
                isPasswordConfirmed = self.user_manager.remove_user(loggedin_user, user_password)
                if(not isPasswordConfirmed):
                   print("The password is incorrect, please try again")
                   self.change_user_account(option, loggedin_user)
                else:
                    self.user_menu.logout()
            case 0:
                self.user_menu.user_menu(loggedin_user)
            case _:
                print("Invalid option.")
                self.change_user_account(option, loggedin_user)
        
        self.user_menu.user_menu(loggedin_user)