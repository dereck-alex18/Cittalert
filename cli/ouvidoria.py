from utils.clear_screen import clear_screen
from cli.authentication import UserManager

class OuvidoriaMenu:
    def __init__(self):
        self.user_manager = UserManager()

    def ouvidoria_menu(self):
        print('''
            ***Ouvidoria***
            [1] Send Complaint
            [2] Edit Complaint
            [3] Visualize Complaints
            [4] Delete Complaint
            [0] Exit
            ''')
    def ouvidoria_options(self, logged_in_user):
         self.ouvidoria_menu()
         from cli.user_menu import UserMenu
         self.user_menu = UserMenu()

         escolha = int(input("Choose one of the options above\n"))
         match escolha:
              case 1: 
                   reclamacao = input("Type your complaint\n")
                   created_reclamacao = self.user_manager.create_ouvidoria(logged_in_user, reclamacao)
                   
                   clear_screen("Creating new Complaint...")

                   if created_reclamacao:
                        print("Complaint successfully sent!")
                   else:
                        print("Something went wrong")
                    
                   self.ouvidoria_options(logged_in_user)
                  
              case 2:
                   self.update_ouvidoria(logged_in_user)
                   self.ouvidoria_options(logged_in_user)
              case 3:
                   self.visualizar_reclamacoes(logged_in_user)
                   self.ouvidoria_options(logged_in_user)
              case 4:
                   self.deletar_reclamacao(logged_in_user)
                   self.ouvidoria_options(logged_in_user)
              case 0:
                   clear_screen("Coming back to user menu...")
                   self.user_menu.user_menu(logged_in_user)
       

    def visualizar_reclamacoes(self, logged_in_user):
         clear_screen("Loading all complaints...")
         self.user_manager.list_ouvidoria(logged_in_user)
           
              

    def deletar_reclamacao(self, loggedin_user):
         list_reclamacao = self.user_manager.list_ouvidoria(loggedin_user)
         if list_reclamacao:
               reclamacao_id = input("Please, type the complaint id you want to delete\n")
               deleted_reclamacao = self.user_manager.delete_ouvidoria(loggedin_user, reclamacao_id)      
               if deleted_reclamacao:
                    clear_screen("Deleting complaint...")
                    print("Complaint successfully deleted")

    def update_ouvidoria(self, loggedin_user):
    
     list_reclamacao = self.user_manager.list_ouvidoria(loggedin_user)
     if list_reclamacao:
          reclamacao_id = input("Please, type the id of the complaint you want to update\n")
          new_complaint = input("Please, type the new complaint\n")
          updated_complaint = self.user_manager.update_ouvidoria(loggedin_user, reclamacao_id, new_complaint)

          clear_screen("Updating complaint...")

          if updated_complaint:
               
               print("Complaint successfully updated")
          else:
               print("Something went wrong, please try again")
                
     else:
          print("No complaints to update")