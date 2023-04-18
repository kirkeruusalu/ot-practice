from sympy import diff, symbols, init_printing
from sympy import sympify
x, y, z = symbols('x, y, z')
init_printing(use_unicode=True)

from entities.equation import Equation
from repositories.equation_repository import EquationRepository
from repositories.user_repository import UserRepository

class Derivative_Service:

    """Class responsible for calculating the derivative"""

    def __init__(self, equation_repository=EquationRepository, current_user=UserRepository):
        self.equation_repository = equation_repository
    

    def find_simple(self, equation):
        equation = sympify(equation)
        return diff(equation)

    def find_product(self, equation):
        equation =  sympify(equation)

    def find_quotient(self, equation):
        equation = sympify(equation)

    