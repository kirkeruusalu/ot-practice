from entities.user import User
from repositories.user_repository import UserRepository
from initialize_database import initialize_database
from services.calculator_service import CalculatorService

repository = UserRepository
calculator = CalculatorService

username = str(input("username:"))
