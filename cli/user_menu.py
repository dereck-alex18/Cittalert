from cli.authentication import UserManager
from utils.clear_screen import clear_screen

class UserMenu():

    def __init__(self):
        self.user_manager = UserManager()

    def user_menu(self, loggedin_user):
        print('''
              ***User Menu***
              [1] Visualize all Alerts
              [2] Create Alerts
              [3] Update Alerts
              [4] Delete Alerts
              [5] Ombudsman
              [6] My Account
              [7] Logout
              ''')
        
        
        try:
            option = int(input('Choose one of the options above\n'))
            self.user_options(option, loggedin_user)
        except ValueError:
            print("Invalid option. Please try again.")
            self.user_menu(loggedin_user)
        
    def user_options(self, option, loggedin_user):
        match option:
            case 1:
                clear_screen("Loading alerts...")
                self.user_manager.list_alerts(loggedin_user)
                self.user_menu(loggedin_user)
            case 2:
                
                alert = input("Please, type the alert you want to report\n")
                created_alert = self.user_manager.create_alert(loggedin_user, alert)

                clear_screen("Creating alert...")
                if created_alert:
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

                    clear_screen("Updating alert...")
                    if updated_alert:
                        print("Alert successfully updated")
                    else:
                        print("Something went wrong, please try again")
                
                else:
                    print("No alerts to update")

               

                self.user_menu(loggedin_user)
            
            case 4:
                list_alerts = self.user_manager.list_alerts(loggedin_user)

                if list_alerts:
                    alert_id = input("Please, type the alert you want to delete\n")
                    deleted_alert = self.user_manager.delete_alert(loggedin_user, alert_id)

                    clear_screen("Deleting alert...")
                    if deleted_alert:  
                        print("Alert successfully deleted")

                self.user_menu(loggedin_user)
            case 5:
                from cli.ouvidoria import OuvidoriaMenu
                clear_screen("Loading ombudsman menu...")
                self.ouvidoria = OuvidoriaMenu()
                self.ouvidoria.ouvidoria_options(loggedin_user)
            case 6:
                clear_screen("Loading account settings menu...")
                from cli.account_settings import UserAccount
                self.account_settings = UserAccount()
                self.account_settings.change_user_account(option, loggedin_user)
            case 7:
                clear_screen("Loggin out...")
                self.logout()
            case _:
                print("Invalid option. Please try again.")
                self.user_menu(loggedin_user)
    
    def logout(self):
        from cli.menu import CLIMenu
        self.initial_menu = CLIMenu()
        self.initial_menu.welcome_message()
        self.initial_menu.initial_menu()
                
