from cli.authentication import UserManager
import os

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
                os.system("clear")
                self.user_manager.list_alerts(loggedin_user)
                self.user_menu(loggedin_user)
            case 2:
                
                alert = input("Please, type the alert you want to report\n")
                created_alert = self.user_manager.create_alert(loggedin_user, alert)

                if created_alert:
                    os.system("clear")
                    print("Alert successfully created")
                else:
                    print("Something went wrong")
                self.user_menu(loggedin_user)
            case 3:
                list_alerts = self.user_manager.list_alerts(loggedin_user)

                if list_alerts:
                    alert_id = input("Please, type the id of the alert you want to update\n")
                    new_alert = input("Please, type the new alert\n")
                    updated_alert = self.user_manager.update_alert(loggedin_user, alert_id, new_alert)

                    if updated_alert:
                        os.system("clear")
                        print("Alert successfully updated")
                    else:
                        os.system("clear")
                        print("Something went wrong, please try again")
                
                else:
                    print("No alerts to update")

               

                self.user_menu(loggedin_user)
            
            case 4:
                list_alerts = self.user_manager.list_alerts(loggedin_user)

                if list_alerts:
                    alert_id = input("Please, type the alert you want to delete\n")
                    deleted_alert = self.user_manager.delete_alert(loggedin_user, alert_id)
                
                    if deleted_alert:
                        os.system("clear")
                        print("Alert successfully deleted")

                self.user_menu(loggedin_user)
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
        self.initial_menu.welcome_message()
        self.initial_menu.initial_menu()
                
