import os
from cli.authentication import UserManager


class UserMenu:

    def __init__(self):
        self.user_manager = UserManager()

    def user_menu(self, loggedInUser):
        print('''
              [1] Visualize all Alerts
              [2] Create Alerts
              [3] Update Alerts
              [4] Delete Alerts
              [5] Ombudsman
              [6] My Account
              [7] Logout
              ''')
