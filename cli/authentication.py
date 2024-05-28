import json

class UserManager:
    def __init__(self) -> None:
        self.data = self.load_all_user_data()
        self.logged_in_user = None

    def load_all_user_data(self):
        with open('data/users.json', 'r') as file:
            user_data = json.load(file)
        return user_data
    
    def manage_id(self, user):
        alert_ids = list(user["alerts"][0].keys())

        if(len(alert_ids) == 0):
            self.id = 1
            return self.id
        
        last_id = int(alert_ids[-1])
        self.id = last_id + 1

        return self.id
    
    def login_user(self, username, password):
        for user in self.data["users"]:
            if user["username"] == username and user["password"] == password:
                self.logged_in_user = user
                return self.logged_in_user
        return False
    
    def get_user(self, username):
        self.data = self.load_all_user_data()
        for user in self.data["users"]:
            if user["username"] == username:
                self.logged_in_user = user
                return self.logged_in_user
        return False
    
    def get_all_usernames(self):
        usernames = []
        for user in self.data["users"]:
            usernames.append(user["username"])
        return sorted(usernames)
    
    def save_user_data(self, username, password):
        new_user = {"username": username, "password": password, "alerts": [{}], "complaints": [{}]}

        for data in self.data["users"]:
            if data["username"] == username:
                return False
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
                user = self.get_user(new_username)
                
                return user
    
    def update_user_password(self, loggedin_user, new_password):
        for user in self.data["users"]:
            if user["username"] == loggedin_user["username"]:
                user["password"] =  new_password
                with open('data/users.json', 'w') as file:
                    json.dump(self.data, file, indent=2)
             
                return True
    
    def remove_user(self, loggedin_user, password):
        for user in self.data["users"]:
            if user["username"] == loggedin_user["username"]:
                if(user["password"] != password):
                    return False
                self.data["users"].remove(user)
                with open('data/users.json', 'w') as file:
                    json.dump(self.data, file, indent=2)
                return True
        return False
    
    def create_alert(self, loggedin_user, alert):
        self.data = self.load_all_user_data()
       
        for user in self.data["users"]:
            if user["username"] == loggedin_user["username"]:
                self.id = self.manage_id(user)       
                user["alerts"][0][self.id] = alert
                with open('data/users.json', 'w') as file:
                    json.dump(self.data, file, indent=2)
                return True
    
    def list_alerts(self, loggedin_user):
        self.data = self.load_all_user_data()
        for user in self.data["users"]:
            if user["username"] == loggedin_user["username"]:
                keys = list(user["alerts"][0].keys())
                values = list(user["alerts"][0].values())
                
                if(len(keys) == 0):
                    print("You don't have any alerts yet")
                    return False
                
                print("List of Alerts:")
                for i in range(len(keys)):
                    print(f"{keys[i]}: {values[i]}")
                return True
        return False
    