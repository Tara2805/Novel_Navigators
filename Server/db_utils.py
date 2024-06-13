import mysql.connector
import json
from config import USER, HOST, PASSWORD

db_name = "Novel_Navigators"

class DatabaseConnectionError(Exception):
    pass


# connect to DB
def connect_to_database(db_name):
    mydb = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    print(f"- Connect - Connected to DB: {mydb}")
    return mydb


# get a random book from the database
def get_random_book_from_database():
    try:
        db_connection = connect_to_database(db_name)
        my_cursor = db_connection.cursor()

        query = """
        SELECT Books.title AS BookName,
        Authors.author_name AS AuthorName,
        Genres.genre_name AS GenreName,
        Reviews.message AS Review
        FROM Books
        JOIN Authors ON Books.author_id = Authors.author_id
        JOIN Genres ON Books.genre_id = Genres.genre_id
        JOIN Reviews ON Books.book_id = Reviews.book_id
        ORDER BY RAND()
        LIMIT 1;"""
        my_cursor.execute(query)
        random_book = my_cursor.fetchone()
        book_dict = {
            "bookTitle": random_book[0],
            "author": random_book[1],
            "genre": random_book[2],
            "review": random_book[3]
            }

        return book_dict

        my_cursor.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


# get book by the specific genre
def get_books_by_genre(genre_id):
    try:
        db_connection = connect_to_database(db_name)
        my_cursor = db_connection.cursor()
        print(f"Connected to DB: {db_name}")

        query = f"""
        SELECT Books.title AS BookName,
        Authors.author_name AS AuthorName,
        Genres.genre_name AS GenreName,
        Reviews.message AS Review
        FROM Books
        JOIN Authors ON Books.author_id = Authors.author_id
        JOIN Genres ON Books.genre_id = Genres.genre_id
        JOIN Reviews ON Books.book_id = Reviews.book_id
        WHERE Genres.genre_id = {genre_id};
        """
        my_cursor.execute(query)
        books = my_cursor.fetchall()
        my_cursor.close()

        books_as_dicts = []
        for book in books:
            book_dict = {
                "bookTitle": book[0],
                "author": book[1],
                "genre": book[2],
                "review": book[3]
            }
            books_as_dicts.append(book_dict)

        return books_as_dicts

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


# retrieve data of a specific book by id
def get_book_by_id(book_id):
    try:
        db_connection = connect_to_database(db_name)
        my_cursor = db_connection.cursor()

        query = f"""
        SELECT Books.title AS BookName,
        Authors.author_name AS AuthorName,
        Genres.genre_name AS GenreName,
        Reviews.message AS Review
        FROM Books
        JOIN Authors ON Books.author_id = Authors.author_id
        JOIN Genres ON Books.genre_id = Genres.genre_id
        JOIN Reviews ON Books.book_id = Reviews.book_id
        WHERE Books.book_id = {book_id};
        """
        my_cursor.execute(query)
        book_reviews = my_cursor.fetchall()
        my_cursor.close()

        book_dict_list = []
        for book in book_reviews:
            book_dict = {
                'bookTitle': book[0],
                'author': book[1],
                'genre': book[2],
                'review': book[3]
            }
            book_dict_list.append(book_dict)
        return book_dict_list

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


# allow user to add review to the DB
def add_review_to_database(book_id, review_message):
    try:
        db_connection = connect_to_database(db_name)
        my_cursor = db_connection.cursor()

        query = """INSERT INTO Reviews (book_id, message) VALUES (%s, %s)"""
        my_cursor.execute(query, (int(book_id), review_message))

        db_connection.commit()
        print("Review added to DB")
        my_cursor.close()
        return True

    except Exception as e:
        print("Error:", e)
        raise DatabaseConnectionError("Failed to insert data into DB")


    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")
    return False


# display all genres from DB
def get_all_genres():
    try:
        db_connection = connect_to_database(db_name)
        my_cursor = db_connection.cursor()

        query = "SELECT * FROM Genres"
        my_cursor.execute(query)
        result = my_cursor.fetchall()

        genres_list = []
        for genre in result:
            genre_dict = {
                "genre_id": genre[0],
                "genre_name": genre[1]
            }
            genres_list.append(genre_dict)

        my_cursor.close()
        return genres_list

    except Exception:
        raise DatabaseConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")














