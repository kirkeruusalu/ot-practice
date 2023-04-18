from entities.user import User
from repositories.user_repository import UserRepository
from initialize_database import initialize_database
from services.user_service import UserService
from services.find_derivative import Derivative_Service

repository = UserRepository()
user = UserService()
derivative = Derivative_Service()
initialize_database()

username = str(input("username:"))

user.create_user(username)

print("new user created")

print("here are all the current users: ", repository.find_all_users())

if str(input("do you want to find by username? (y/n)")) == "y":
    name = str(input("enter username to look for: "))
    print(repository.find_by_username(name))


hello = input("write equation: ")
print(derivative.find_simple(hello))

while input("do you want to stop? (y/n)") == "n":
    hello = input("write a very simple equation with variable x: ")
    print(derivative.find_simple(hello))
    
