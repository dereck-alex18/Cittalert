from utils.clear_screen import clear_screen
from cli.authentication import UserManager

class UserAccount:
    def __init__(self):
        self.user_manager = UserManager()

    def user_account_menu(self):
        print('''
              ***Account Settings Menu***
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

        try:
            option = int(input("Please choose one of the options above\n"))
        except ValueError:
            print("Invalid option. Please try again.")
            self.change_user_account(option, loggedin_user)

        match option:
            case 1:
                clear_screen("Loading all users...")
                all_users = self.user_manager.get_all_usernames()
                print("All Usernames: \n")
             
                for index, user in enumerate(all_users, start=1):
                    print(f"{index} - {user}")
                self.change_user_account(option, loggedin_user)
            case 2:
                new_username = input("Please enter your new username\n")
                clear_screen("Changing username...")

                user = self.user_manager.update_user_username(loggedin_user, new_username)
                if(not user):
                   print("The username is already taken, please choose another one")
                   self.change_user_account(option, loggedin_user)
                else:
                   
                   print("Username successfully changed")
                   loggedin_user = user

                self.change_user_account(option, loggedin_user)
            case 3:
                new_password = input("Please enter your new password\n")
                isChanged = self.user_manager.update_user_password(loggedin_user, new_password)
                clear_screen("Changing password...")
                if(not isChanged):
                   print("The password is already taken, please choose another one")
                 
                else:
                   print("Password successfully changed")

                self.change_user_account(option, loggedin_user)
            case 4:
                user_password = input("Please enter your password to delete your account\n");
                isPasswordConfirmed = self.user_manager.remove_user(loggedin_user, user_password)
                if(not isPasswordConfirmed):
                   print("The password is incorrect, please try again")
                else:
                    clear_screen("Deleting your account... Goodbye :(")
                    self.user_menu.logout()

                self.change_user_account(option, loggedin_user)
            case 0:
                clear_screen("Coming back to user menu...")
                self.user_menu.user_menu(loggedin_user)
            case _:
                print("Invalid option. Please try again.")
                self.change_user_account(option, loggedin_user)
        
        