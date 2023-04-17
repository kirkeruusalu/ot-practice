from entities.user import User
from repositories.user_repository import UserRepository
from initialize_database import initialize_database
from services.calculator_service import CalculatorService

repository = UserRepository()
calculator = CalculatorService()

username = str(input("username:"))

calculator.create_user(username)

print("new user created")

print("here are all the current users: ", repository.find_all_users())

if str(input("do you want to find by username? (y/n)")) == "y":
    name = str(input("enter username to look for: "))
    print(repository.find_by_username(name))
