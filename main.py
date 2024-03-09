from cli.authentication import UserManager

if __name__ == '__main__': 
    user_manager = UserManager()
    all_users = user_manager.load_all_user_data()
    
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    user_manager.save_user_data(username, password)