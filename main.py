from cli.menu import CLIMenu

def main():
    menu = CLIMenu()
    menu.welcome_message()
    menu.initial_menu()

if __name__ == '__main__': 
    main()