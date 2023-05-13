from tkinter import messagebox, constants
import tkinter as tk
from services.user_service import user_service, InvalidError, DoesNotExistError
from services.find_derivative import derivative_service, FormattingError

class DerivativeFinder:
    """This class is responsible for the users view of the equation entered and the derivative that is found
    
    """

    
    def __init__(self, root, handle_login):
        self._root = root
        self._handle_return_to_login = handle_login
        self._frame = None

        self._user = user_service.find_logged_in_user()
        self._equation_entered = None
        self._derivative = None
        

        self._start()

    def _start(self):
        self._frame = tk.Frame(master=self._root)
        header = tk.Label(master=self._frame, text="Here you can type in an equation: ")
        equation =tk.Label(master=self._frame, text="Equation: ")
        _equation_entered = tk.Entry(master=self._frame)

        calculate_result_button = tk.Button(master=self._frame, text="Calculate", command=self._handle_calculation)
        header.grid(columnspan=3, sticky=(constants.N), padx=5, pady=5)
        equation.grid(padx=5, pady=5)
        _equation_entered.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        calculate_result_button.grid(columnspan=3)

        self._frame.grid_columnconfigure(1, weight=2, minsize=300)
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()
    
    def _handle_calculation(self):
        derivative_service.find_simple(self._equation_entered)

    def _handle_logout(self):
        user_service.log_out()
        self._handle_return_to_login()

