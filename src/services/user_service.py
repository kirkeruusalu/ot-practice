import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from entities.user import User
from entities.equation import Equation
from repositories.user_repository import user_repository



class UserService:
    """This class is responsible for application logic"""

    def __init__(self, user_repository=user_repository):
        self._user_repository = user_repository
        self._user = None

    def create_user(self, username):
        is_there_user = self._user_repository.find_by_username(username)

        if is_there_user:
            raise InvalidError("this username exists, choose a new one")
        
        self._user_repository.create_user(User(username))

    def delete_user(self, username):
        is_there_user = self._user_repository.find_by_username(username)
        if not is_there_user:
            self._user_repository.delete_user(User(username))
        else:
            raise DoesNotExistError("this username does not exist")
        
    def log_in(self, username):
        is_there_user = self._user_repository.find_by_username(username)
        if not is_there_user:
            raise DoesNotExistError("this username does not exist")
        
        self._user = is_there_user
        return self._user
    
    def find_logged_in_user(self):
        return self._user
        

    def log_out(self, username):
        self._user = None

class InvalidError(Exception):
    pass

class DoesNotExistError(Exception):
    pass

    
user_service = UserService(user_repository)
    


        

        
        




