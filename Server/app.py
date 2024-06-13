# define API endpoints
from flask import Flask, jsonify, request  # importing Flask and then using the jsonify function to create a JSON response
import db_utils  # importing db_utils to connect our Flask application with our database


app = Flask(__name__)  # creating the Flask application

@app.route('/')
def index():
    return "Welcome to the Novel Navigator!"


# get all genres
@app.route('/genres', methods=['GET'])
def all_genres():
    genres = db_utils.get_all_genres()
    return jsonify(genres)


# get a random book info
@app.route('/random_book', methods=['GET'])
def get_random_book():
    random_book = db_utils.get_random_book_from_database()
    return jsonify(random_book)


# get books by genre
@app.route('/genres/<int:genre_id>/books', methods=['GET'])
def get_books_by_genre(genre_id):
    books = db_utils.get_books_by_genre(genre_id)
    return jsonify(books)

# get book by book id
@app.route('/book/<int:book_id>', methods=['GET'])
def books_by_book_id(book_id):
    books = db_utils.get_book_by_id(book_id)
    return jsonify(books)


# add review
@app.route('/book/add_review', methods=['POST'])
def add_book_review():
    review_data = request.get_json()
    success = db_utils.add_review_to_database(
        book_id = review_data['book_id'],
        review_message=review_data['review_message']
    )
    if success:
        print("Book review added successfully!")
    else:
        print("Failed to add book review.")



if __name__ == '__main__':
    app.run(debug=True)
