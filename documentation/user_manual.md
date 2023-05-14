# User Manual

## Configuration
The name of the database file is automatically configured through the .env file in the application's root directory, and the file will be created the directory called data. In the .env file, the file name that is used can also be changed.

The following file format is used:

```bash
DATABASE_FILE=database.sqlite
```

## Starting the application

1. Install dependencies through the command line with:

```bash
poetry install
```

2. Initialize everything with: 

```bash
poetry run invoke begin
```

3. Start the application with: 

```bash
poetry run invoke start
```

## Login
When starting the application, the first view is the login view.
![login_view](https://github.com/kirkeruusalu/ot-practice/assets/128533486/85b33a19-dc0f-4dc8-bc5e-df12fdba0d5a)

If you have an account, you can enter your username and press log in. Otherwise, click on create new user and log in.

## Creating a new user
After clicking create new user, this view comes: 
![create_account_view](https://github.com/kirkeruusalu/ot-practice/assets/128533486/91a0494e-d8b2-44f1-a678-d46efe3e2a6e)

You can type in a unique username to create your account. If this username is already in use, you will be notified and you must choose another one. After this, you will be redirected to the login view once again. Then you can now log in.


## Find derivative
After logging in successfully, you will be taken to a page where you can insert an equation, for which the derivative will be found. If this equation is in an invalid format, you will be notified and you must type in another one.


