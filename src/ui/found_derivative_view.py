from services.user_service import DoesNotExistError, user_service
import tkinter as tk
from tkinter import ttk, messagebox, constants
from sympy import symbols, diff
from ui.derivative_finder_view import DerivativeFinder

class DerivativeView:
    """A class that handles what the UI looks like for displaying the derivative
    """

    def __init__(self, root, handle_derivative, derivative):
        self._root = root
        self._handle_derivative = handle_derivative
        self._derivative = derivative
        self._frame = None
        self._derivative_label = None

        self._start()

    def _start(self):
        self._frame = tk.Frame(master=self._root)
        header = tk.Label(master=self._frame, text="The derivative is:")
        self._derivative_label = tk.Label(master=self._frame, text=self._derivative)

        back_button = tk.Button(self._root, text = "Back", command=self._handle_back_button)

        header.grid(columnspan=2, sticky=(tk.N), padx=5, pady=5)
        self._derivative_label.grid(row=1, column=0, sticky=(tk.E, tk.W), padx=5, pady=5)

        self._frame.grid_columnconfigure(0, weight=2, minsize=300)
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _handle_back_button(self):
        derivative_finder_view = DerivativeFinder(self._root, self._handle_derivative, self._derivative)
        self.destroy()
        self._handle_derivative(derivative_finder_view)
        

       
