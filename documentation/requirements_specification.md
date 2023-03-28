# Requirements Specification

## Purpose of the application
My application is a derivative and integral calculator to help users with solving their necessary mathematical equations. It can be used by several registered users, who can keep track of equations they have previously entered if they wish to do so.

## Users
There is a regular user role, where the current user can create an account, and later log in to it using their credentials. The user can only access their information.

This will initially be done with a text interface, but will hopefully later be a graphical user interface.
An extension could be an administrative role, where the root user can delete and access all the other accounts.

## Functionalities

### Basic functionalities
- Before logging in:
  - The user can create a username that is constrained by some factors (e.g. length)
  - If there is already the same username in the system, the user will be notified of this and have to choose a different one.
  - Potentially also a password will be asked of the user as an extension. This is initially not in the plan, as the infromation displayed by the applicatoin is not sensitive information, and only for personal academic development.
- The user logs in.
  - The user is asked if they wish to review previous equations, if they wish to find a derivative or a new equation, or if they wish to find an integral of an equation.
  - If they wish to review previous equations:
     - The user can view a list of their previous saved equations
     - The user can removed any saved equations (for example, if they feel like they have understood the content).
  - If they wish to find a derivative:
     - The user is redirected to a window where they can write in an equation (if they equation is mathematically invalid, they will be told so). Then, the derivative of the equation will be presented to them.
  - If they wish to find an integral:
     - The user is also redirected to a window where they can write in an equation, then an integral of this equation will be presented to them.

- After the derivative/integral is presented to the user, they will be asked whether they want to save it for later review. In this case, both the original equation and the result will be saved. If they do not wish to save, the result will be deleted from memory.
- The user can log out when the user wishes to exit the application.
- The user can also choose to delete their account and all of the infromation associated with it.

### Further development ideas
If time permits:
- The original function will be graphed along with the derivative/integral.
- Every separate user has a special space where they can add notes/comments to themselves (about a particular equation or topic in general).
- The system will log out the user automatically after a certian time period of inactivity.

