"""creates a random table of records with 'no_lines' database for testing purposes"""

from random import randint
import sqlite3


def create_db(no_lines):
    with sqlite3.connect("a35_db_search//big_database.db") as connection:
        my_cursor = connection.cursor()
        my_cursor.execute("""
                        CREATE TABLE Records(
                            id          INTEGER PRIMARY KEY,
                            name        text
                            );
                        """)
        for _ in range(no_lines):
            name_value = ("NAME" + str(randint(1, 100)))
            my_cursor.execute(f"""INSERT INTO Records (name) VALUES (:name);""", {"name":name_value})



if __name__ == "__main__":
    create_db(1_000_000)