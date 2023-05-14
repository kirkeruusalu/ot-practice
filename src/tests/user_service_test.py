import unittest
from services.user_service import UserService
from entities.user import User
from repositories.user_repository import UserRepository


test_repository = UserRepository()


class TestLoginService(unittest.TestCase):

    def setUp(self):
        self.test_user_service = UserService(test_repository)
        test_repository.delete_all()

    def test_create_user(self):
        self.test_user_service.create_user("kirke")
        is_there = test_repository.find_by_username("kirke")
        self.assertEqual(is_there.username, "kirke")
    
    def test_create_user_exists(self):
        self.test_user_service.create_user("kirke")
        with  self.assertRaises(Exception) as context:
            self.test_user_service.create_user("kirke")
            
        self.assertTrue("this username exists, choose a new one" in str(context.exception))
     



