from database_connection import get_database_connection

def create_users_table(connection):
    cursor = connection.cursor()

    cursor.execute("""
        create table if not exists users (
            username text primary key
        );
    """)

    connection.commit()

def drop_users_table(connection):
    cursor = connection.cursor()

    cursor.execute("""
        drop table if exists users;
    """)

    connection.commit()

def initialize_database():

    connection = get_database_connection()

    drop_users_table(connection)
    create_users_table(connection)

if __name__ == "__main__":

    initialize_database()