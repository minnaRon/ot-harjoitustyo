from database_connection import get_database_connection


# using in class:
# from initialize_database import initialize_database
# initialize_database()


def drop_tables(connection):
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS Practices;")
    cursor.execute("DROP TABLE IF EXISTS Translations;")
    cursor.execute("DROP TABLE IF EXISTS Persons;")
    cursor.execute("DROP TABLE IF EXISTS Words;")

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
                    word_orig_id INTEGER REFERENCE Words,
                    word_transl_id INTEGER REFERENCE Words
                    );
                    ''')

    cursor.execute(''' CREATE TABLE Persons (
                    id INTEGER PRIMARY KEY,
                    name TEXT UNIQUE NOT NULL,
                    password INTEGER
                    );
                    ''')

    cursor.execute(''' CREATE TABLE Practices (
                    id INTEGER PRIMARY KEY,
                    person_id INTEGER REFERENCE Persons NOT NULL,
                    translation_id INTEGER REFERENCE Translations NOT NULL,
                    practicing_points_left INTEGER
                    );
                    ''')
    connection.commit()


def initialize_database():
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)


if __name__ == '__main__':
    initialize_database()
