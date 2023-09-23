import sqlite3

try:
    bookDB = sqlite3.connect("bookDB.db")
    cursor = bookDB.cursor()

    listings_schema = """
                CREATE TABLE listings(
                id INTEGER PRIMARY KEY,
                listersEmail TEXT,
                title TEXT,
                course TEXT,
                condition TEXT,
                price INTEGER,
                extraInfo TEXT
                );
                """
    discussions_schema = """
                CREATE TABLE discussions(
                id INTEGER PRIMARY KEY,
                bookID INTEGER,
                message TEXT
                );
                """

    results = cursor.execute("DROP TABLE IF EXISTS listings;")
    results = cursor.execute(listings_schema)

    results = cursor.execute("DROP TABLE IF EXISTS discussions;")
    results = cursor.execute(discussions_schema)


    print("Database schema established successfully")
except sqlite3.Error as error:
    print('Error occurred - ', error)
finally:
    bookDB.close()
