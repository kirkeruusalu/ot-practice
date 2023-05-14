import unittest
from services.user_service import UserService
from entities.user import User
from repositories.user_repository import UserRepository
from services.find_derivative import Derivative_Service
from repositories.equation_repository import EquationRepository

test_repository = UserRepository()
test_repository2 = EquationRepository()

#class TestDerivativeService(unittest.TestCase):
 #   def setUp(self):
  #      self.test_derivative_finder = Derivative_Service(