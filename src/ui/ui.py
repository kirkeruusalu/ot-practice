from tkinter import Tk
from ui.login_view import LoginView
from ui.create_user_view import CreateUserView
from ui.derivative_finder_view import DerivativeFinder


class UI:
    """This class is responsible for moving between the different
        windows visible to the user
    """

    def __init__(self, root):
        """Class constructor, arguments: the root frame
        """
        self._root = root
        self._current = None

    def initial(self):
        """The view that the user sees when opening the app
        """
        self._show_login()

    def _hide_current(self):
        if self._current:
            self._current.destroy()

    def _handle_create_user(self):
        self._show_create_user_view()

    def _handle_login(self):
        self._show_login()

    def _handle_derivative(self):
        self._show_find_derivative_view()
    
    def _show_login(self):
        self._hide_current()
        self._current = LoginView(self._root, self._handle_create_user, self._handle_derivative)
        
    def _show_create_user_view(self):
        self._hide_current()
        self._current = CreateUserView(self._root, self._handle_login)
    
    def _show_find_derivative_view(self):
        self._hide_current()
        self._current = DerivativeFinder(self._root, self._handle_login)
        

    

    