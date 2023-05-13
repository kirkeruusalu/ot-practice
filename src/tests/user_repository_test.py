import unittest
from repositories.user_repository import user_repository
from entities . user import User

test_repository = user_repository


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        test_repository.delete_all()
        self.user_kirke = User("kirke")
        self.user_laura = User("laura")

    def test_create_user(self):
        test_repository.create_user(self.user_kirke)
        is_there = test_repository.find_by_username(self.user_kirke.username)

        self.assertEqual(is_there.username, self.user_kirke.username)

    def test_find_by_username_returns_None(self):
        is_there = test_repository.find_by_username(self.user_kirke.username)

        self.assertEqual(is_there, None)
    
    def test_delete_all(self):
        test_repository.create_user(self.user_kirke)
        test_repository.create_user(self.user_laura)
        test_repository.delete_all()
        is_there = test_repository.find_all_users()
        self.assertEqual(len(is_there), 0)

    def test_delete_one(self):
        test_repository.create_user(self.user_kirke)
        test_repository.delete_user("kirke")
        is_there = test_repository.find_by_username("kirke")
        self.assertEqual(is_there, None)

    def test_find_all_users_is_correct(self):
        test_repository.create_user(self.user_kirke)
        test_repository.create_user(self.user_laura)
        is_there = test_repository.find_all_users()

        self.assertEqual(len(is_there,), 2)
