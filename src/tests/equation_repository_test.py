import unittest
from repositories.equation_repository import equation_repository
from entities . equation import Equation
from repositories.user_repository import user_repository
from entities . user import User

test_repository = equation_repository
test_repository2 = user_repository


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        test_repository.delete_all()
        test_repository2.delete_all()
        self.user_kirke = User("kirke")
        self.equation = Equation("3*x", "kirke")

   # def test_delete_equation(self):
    #    test_repository.add_equation(self.equation)
     #   test_repository.delete_equation(self.equation)
      #  find = test_repository.give_all_equations_for_user()
#
 #       self.assertEqual(len(find), 0)