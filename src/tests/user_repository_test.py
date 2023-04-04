import unittest
from repositories.user_repository import user_repository
from entities . user import User

#test_repository = UserRepository()
class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.user_kirke = User("kirke")
        

    def test_create_user(self):
        user_repository.create_user(self.user_kirke)
        is_there = user_repository.find_by_username(self.user_kirke.username)

        self.assertEqual(is_there["username"], self.user_kirke.username)



