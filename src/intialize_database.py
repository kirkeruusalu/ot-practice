from database_connection import get_database_connection

def create_users_table(connection):
    cursor = connection.cursor()

    cursor.execute()
    connection.commit()

def initialize_database():

    connection = get_database_connection()

if __name__ == "__main__":
    initialize_database()