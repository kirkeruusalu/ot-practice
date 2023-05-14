# Requirements Specification

## Purpose of the application
My application is a derivative calculator to help users with solving their necessary mathematical equations. It can be used by several registered users, whose username is recorded in an SQLite database. 

## Users
There is a regular user role, where the current user can create an account, and later log in to it using their credentials. The user can only access their information.
For this, there is a graphical user interface.
An extension could be an administrative role, where the root user can delete and access all the other accounts.

## Functionalities

### Basic functionalities
- Before logging in:
  -  The user can create a unique username that will be recorded in the database.
  -  If there is already the same username in the system, the user will be notified of this and have to choose a different one.
  -  No password is asked, because this application does not contain sensitive information.
-   The user logs in.
  - The user is redirected to a window where they can write in an equation (if they equation is mathematically invalid, they will be told so).  Then the derivative of the equation will be presented to them.

- After the derivative/integral is presented to the user, they can choose to go back to the window that asked them for an equation. Then, they can find a derivative of another equation.
- The user can log out when the user wishes to exit the application.

### Further development ideas
- The original function could be graphed along with the derivative.
- Every separate user has a special space where they can add notes/comments to themselves (about a particular equation or topic in general).
- The system will log out the user automatically after a certain time period of inactivity.

