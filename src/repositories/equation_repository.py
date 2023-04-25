from pathlib import Path
from entities . equation import Equation
from entities . user import User
from repositories.user_repository import UserRepository
from database_connection import get_database_connection

class EquationRepository:
    """A class responsible for database operations related to equations and their results"""

    def __init__(self):
        self._connection = get_database_connection()
    
    def add_equation(self, user=User, equation=Equation):
        cursor = self._connection.cursor()

        cursor.execute("""
                insert into equations (username, equation) values (?, ?)
                """,
                (user.username, equation.equation)      
            )
        self._connection.commit()

    def give_equation(self, user=User, equation=Equation):
        cursor = self._connection.cursor()

        cursor.execute("""
            select (username, equation) from equations where username = user.username and equation = equation.equation
            """)
        
        return cursor.fetchone()
    
    def give_all_equations_for_user(self, user=User):
        cursor = self._connection.cursor()

        cursor.execute("""
            select (username, equation) from equations where username = user.username)
            """)
        
        return cursor.fetchall()
    
    def delete_equation(self, user=User, equation=Equation):
        cursor = self._connection.cursor()

        cursor.execute("""
            delete from equations where username = user.username and equation = equation.equation
            """)
        
        self._connection.commit()

    
        
        