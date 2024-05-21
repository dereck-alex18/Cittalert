from cli.authentication import UserManager

class UserAccount:
    def __init__(self):
        self.user_manager = UserManager()

    def user_account_menu(self):
        print('''
              [1] Change Username
              [2] Change Password
              ''')
       
    def change_user_account(self, option, loggedin_user):
        self.user_account_menu()
        option = int(input())
    
        
        match option:
            case 1:
                new_username = input("Please enter your new username\n")
                isChanged = self.user_manager.update_user_username(loggedin_user, new_username)
                if(not isChanged):
                   print("The username is already taken, please choose another one")
                   self.change_user_account(option, loggedin_user)
                else:
                   print("Username successfully changed")