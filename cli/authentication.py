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
        new_user = {"username": username, "password": password}

        for data in self.data["users"]:
            if data["username"] == username:
                return False

        self.data["users"].append(new_user)
        with open('data/users.json', 'w') as file:
            json.dump(self.data, file, indent=2)
        
        return True