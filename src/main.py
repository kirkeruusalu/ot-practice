from entities.user import User
from repositories.user_repository import UserRepository
from initialize_database import initialize_database
from services.user_service import UserService
from services.find_derivative import Derivative_Service
from tkinter import Tk
from ui.ui import UI

#repository = UserRepository()
#user = UserService()
#derivative = Derivative_Service()
#initialize_database()

#username = str(input("username:"))
#user.create_user(username)

#print("new user created")

#print("here are all the current users: ", repository.find_all_users())

#if str(input("do you want to find by username? (y/n)")) == "y":
 #   name = str(input("enter username to look for: "))
  #  print(repository.find_by_username(name))

#while True:
 #   hello = input("write a very simple equation with variable x. use python syntax: ")
  #  print(derivative.find_simple(hello))
#
 #   result = input("do you want to find another one? (y/n)")
  #  if result != "y":
   #     if result == "n" or result == "N":
    #        print("okay, you will now exit the application")
     #       break    
      #  else:
       #      print("i dont know what you mean by that, so i will continue asking you for an equation")


window = Tk()
window.title("Derivative Calculator")
interface = UI(window)
interface.initial()
window.mainloop()
