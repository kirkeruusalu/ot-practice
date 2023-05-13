from tkinter import messagebox, constants
import tkinter as tk
from services.user_service import user_service, InvalidError, DoesNotExistError

class CreateUserView:
    """This class is responsible for what the view is like if the user creates a new account
    
    """

    def __init__(self, root, handle_login):
        self._root = root 
        self._handle_login = handle_login
        self._frame = None
    
        self._username = None
        self._start()

    def _start(self):
        self._frame = tk.Frame(master=self._root)
        header = tk.Label(master=self._frame, text="You can create a new account")
        username =tk.Label(master=self._frame, text="What do you want your username to be?")
        self._username_entered = tk.Entry(master=self._frame)

       
        create_account_and_login_button= tk.Button(master=self._frame, text="Create new account and log in", command = self._handle_create_and_log_in_button)

        header.grid(columnspan=3, sticky=(constants.N), padx=5, pady=5)
        username.grid(padx=5, pady=5)
        self._username_entered.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
    

        create_account_and_login_button.grid(columnspan=3)

        self._frame.grid_columnconfigure(1, weight=2, minsize=300)
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _handle_create_and_log_in_button(self):
        usernamevalue = self._username_entered.get()
        if usernamevalue:
            try:
                user_service.create_user(usernamevalue)
                self._handle_login()
            except InvalidError:
                self._error_message("This one exists")
    
    def _error_message(self, message):
           messagebox.showerror("Error", message)
