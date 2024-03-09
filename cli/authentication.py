import json

class UserManager:
    def __init__(self) -> None:
        self.data = self.load_all_user_data()

    def load_all_user_data(self):
        with open('data/users.json', 'r') as file:
            user_data = json.load(file)
        return user_data
    
    def save_user_data(self, username, password):
        new_user = {"username": username, "password": password}
        self.data["users"].append(new_user)
        with open('data/users.json', 'w') as file:
            json.dump(self.data, file, indent=2)