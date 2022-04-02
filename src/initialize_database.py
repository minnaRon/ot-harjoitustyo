from database_connection import get_database_connection

'''
using in class:
from initialize_database import initialize_database
initialize_database()
'''

def drop_tables(connection):
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS AddingTableHereLater;")
    connection.commit()

def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute(''' CREATE TABLE AddingTableHereLater
                        (someColumn TEXT PRIMARY KEY);
                    ''')
    connection.commit()

def initialize_database():
    connection = get_database_connection
    drop_tables(connection)
    create_tables(connection)

if __name__ == '__main__':
    initialize_database()
