from services.user_service import DoesNotExistError, user_service
import tkinter as tk
from tkinter import ttk, messagebox, constants


class LoginView:
    """A class that handles what the UI looks like if the user wishes to log in
    """

    def __init__(self, root, handle_create_user, handle_derivative):
        self._root = root
        self._handle_create = handle_create_user
        self._handle_find = handle_derivative
        self._frame = None
        self._style = None
        self._username = None

        self._start()

    def _start(self):
        self._frame = tk.Frame(master=self._root)
        header = tk.Label(master=self._frame, text="This is the derivative calculator, nice to see you here!")
        username =tk.Label(master=self._frame, text="Username: ")
        self._username_entered = tk.Entry(master=self._frame)

        login_button = tk.Button(master=self._frame, text="Login", command=self._handle_login_button)
        create_user_button= tk.Button(master=self._frame, text="Create new user", command = self._handle_create)

        header.grid(columnspan=3, sticky=(constants.N), padx=5, pady=5)
        username.grid(padx=5, pady=5)
        self._username_entered.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        
        login_button.grid(columnspan=3,)

        create_user_button.grid(columnspan=3)

        self._frame.grid_columnconfigure(1, weight=2, minsize=300)
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _handle_login_button(self):
        username_value = self._username_entered.get()

        if username_value:
            try:
                user_service.log_in(username_value)
                self._handle_create()
                self._handle_find()
            except DoesNotExistError:
                self._errormessage("Invalid. Try again")

    def _errormessage(self, message):
        messagebox.showerror("Error,", message)
    
    



    