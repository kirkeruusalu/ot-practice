from tkinter import messagebox, constants
from tkinter import ttk
import tkinter as tk
from services.user_service import user_service, InvalidError, DoesNotExistError
from services.find_derivative import derivative_service, FormattingError
from ui.found_derivative_view import DerivativeView

class DerivativeFinder:
    """This class is responsible for the users view of the equation entered and the derivative that is found
    
    """

    
    def __init__(self, root, handle_login, handle_found_derivative):
        self._root = root
        #self._handle_calculate_button = None
        self._handle_found_derivative = handle_found_derivative
        self._frame = None
        self._handle_login = handle_login
        self._equation_entered = None
        self._start()

    def _start(self):
        self._frame = tk.Frame(master=self._root)
        header = tk.Label(master=self._frame, text="""Here you can type in an equation. Remember to use Python format, e.g. if you want the derivative of 3x, write it as 3*x :)))
                            YOU ONLY GET ONE cos im a dumb bitch who doesnt know how to add a back button
                          """)
       
        self._equation_entered = tk.Entry(master=self._frame)

        calculate_result_button = tk.Button(master=self._frame, text="Calculate", command=self._handle_calculate_button)
        header.grid(columnspan=3, sticky=(constants.N), padx=5, pady=5)
      
        self._equation_entered.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        calculate_result_button.grid(columnspan=3)

        self._frame.grid_columnconfigure(1, weight=2, minsize=300)
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()
    
    def _handle_calculate_button(self):
        equation = self.get_equation_entered()
        try:                 
            result = derivative_service.find_simple(equation)
            derivative_view = DerivativeView(self._root, self._handle_found_derivative, result)
            self._handle_found_derivative(derivative_view)
        except FormattingError:
            self._error_message("Wrong format, try again")
        

    def _error_message(self, message):
           messagebox.showerror("Error", message)


    def get_equation_entered(self):
        return self._equation_entered.get()
    
    
