from database_connection import get_database_connection

'''
using in class:
from initialize_database import initialize_database
initialize_database()
'''

def drop_tables(connection):
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS Words;")
    cursor.execute("DROP TABLE IF EXISTS Translations;")

    connection.commit()

def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute(''' CREATE TABLE Words (
                    id INTEGER PRIMARY KEY,
                    word TEXT,
                    language TEXT
                    );
                    ''')

    cursor.execute(''' CREATE TABLE Translations (
                    id INTEGER PRIMARY KEY,
                    word_orig_id INTEGER,
                    word_transl_id INTEGER
                    );
                    ''')
    connection.commit()

def initialize_database():
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)

if __name__ == '__main__':
    initialize_database()
