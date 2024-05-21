import json

class UserManager:
    def __init__(self) -> None:
        self.data = self.load_all_user_data()
        self.logged_in_user = None

    def load_all_user_data(self):
        with open('data/users.json', 'r') as file:
            user_data = json.load(file)
        return user_data
    
    def login_user(self, username, password):
        for user in self.data["users"]:
            if user["username"] == username and user["password"] == password:
                self.logged_in_user = user
                return self.logged_in_user
        return False
    
    def save_user_data(self, username, password):
        new_user = {"username": username, "password": password, "alerts": [{}], "complaints": [{}]}

        for data in self.data["users"]:
            if data["username"] == username:
                return False

        print(self.data["users"][1])
        self.data["users"].append(new_user)
        with open('data/users.json', 'w') as file:
            json.dump(self.data, file, indent=2)
        
        return True
    
    def update_user_username(self, loggedin_user, new_username):
        for user in self.data["users"]:
            if user["username"] == new_username:
                return False
        for user in self.data["users"]:
            if user["username"] == loggedin_user["username"]:
                user["username"] =  new_username
                with open('data/users.json', 'w') as file:
                    json.dump(self.data, file, indent=2)    
                return True
    
    #adapt this method to change the password
    def update_user_password(self, loggedin_user, new_username):
        for user in self.data["users"]:
            if user["username"] == new_username:
                return False
        for user in self.data["users"]:
            if user["username"] == loggedin_user["username"]:
                user["username"] =  new_username
                with open('data/users.json', 'w') as file:
                    json.dump(self.data, file, indent=2)    
                return True
 
 
    