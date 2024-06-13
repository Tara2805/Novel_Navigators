# import requests to make requests to the API
import requests
import json
import random

end_session_graph = """  
                 .--.   _
             .---|__| .((\\=.
          .--|===|--|/    ,(,
          |  |===|  |\\      y
          |%%|   |  | `.__,'   Enjoy your reading!
          |  |   |  |/|  | \\\\`----.
          |  |   |  ||\\  \\  |___.'_
         _|  |   |__||,\\  \\-+-._.' )_
        / |  |===|--|\\  \\  \\      /  \\\\
       /  `--^---'--' `--`-'---^-'    \\\\
      '================================` """

'''
Purpose: get data of a random book
'''
def get_random_book():
    response = requests.get(
        url="http://127.0.0.1:5000/random_book",
        headers = {'content-type': 'application/json'}
    )
    book_data = response.json()
    book_title = book_data["bookTitle"]
    genre = book_data["genre"]
    author = book_data["author"]
    review = book_data["review"]

    print('\33[32m⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚ \33[0m')
    print("Here's our recommendation:")
    print(f"\033[32m\n{book_title}\033[0m")
    print(f"author: {author} / genre: {genre}")
    print(f"Reviews:\n\33[32m⊚\33[0m {review}\n")
    print('\33[32m\n⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚\n \33[0m')


'''
Purpose: get data of a specific book by the book ID
'''
def get_book_by_id(book_id):
    response = requests.get(
        url="http://127.0.0.1:5000/book/{}".format(book_id),
        headers = {'content-type': 'application/json'}
    )
    book_data_list = response.json()
    if len(book_data_list) == 0:
        print("No data found!")
    else:
        book_title = book_data_list[0]["bookTitle"]
        genre = book_data_list[0]["genre"]
        author = book_data_list[0]["author"]
        print('\33[32m⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚ \33[0m')
        print(f"\033[32m\n{book_title}\033[0m")
        print(f"Author: {author} / Genre: {genre}")
        print("Reviews:")
        # using a for loop to ensure all relevant reviews will be printed out
        for book_data in book_data_list:
            review = book_data["review"]
            print(f"\33[32m⊚\33[0m {review}")
        print('\33[32m\n⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚\n \33[0m')


'''
Purpose: get books by genre, then return 1 book by random using the Python Random randint method()
'''
def get_book_by_genre(genre_id):
    try:
        response = requests.get(
            url="http://127.0.0.1:5000//genres/{}/books".format(genre_id),
            headers={'content-type': 'application/json'}
        )

        response.raise_for_status()  # Raise an exception for any HTTP error

        book_data = response.json()
        num_books = len(book_data)

        if num_books > 0:
            random_number = random.randint(0, num_books - 1)
            book = book_data[random_number]

            book_title = book["bookTitle"]
            genre = book["genre"]
            author = book["author"]
            review = book["review"]

            print('\33[32m⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚ \33[0m')
            print(f"\033[32m\n{book_title}\033[0m")
            print(f"author: {author} / genre: {genre}")
            print(f"Reviews:\n {review}\n")
            print('\33[32m\n⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚\n \33[0m')
        else:
            print(f"No books found for genre ID {genre_id}")
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except requests.exceptions.RequestException as e:
        print(f"Request exception occurred: {e}")
    except (ValueError, KeyError) as e:
        print(f"Error processing JSON data: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


'''
Purpose: add a new book review
'''
def add_book_review(book_id, review_message):
    book_data = {
        "book_id": book_id,
        "review_message": review_message
    }
    requests.post(
        url="http://127.0.0.1:5000/book/add_review",
        headers={'content-type': 'application/json'},
        data = json.dumps(book_data)
    )


''' 
Purpose: display all genres
'''
def display_genre_list():
    try:
        response = requests.get(
            url="http://127.0.0.1:5000/genres",
            headers={'content-type': 'application/json'}
        )
        response.raise_for_status()  # Raise an exception for any HTTP error

        genres = response.json()

        if genres:
            print("List of Genres:")
            for index, genre in enumerate(genres, start=1):
                genre_name = genre.get("genre_name")
                print(f"{index}. {genre_name}")
        else:
            print("No genres found.")
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except requests.exceptions.RequestException as e:
        print(f"Request exception occurred: {e}")
    except (ValueError, KeyError) as e:
        print(f"Error processing JSON data: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")




def run():
    # run the session
    while True:
        # use boolean "True" to check if the session has ended
        print(
            "What would you like to do?")
        user_choice = input("Type 1 to get a random book recommendation\nType 2 to look up a book by book id\nType 3 to add a book review\n")
        # this is designed so that after user added a book review, they can look up that book by id to see if their review was added

        if user_choice == "1":
            user_genre_choice = input("Is there a specific genre you prefer? Press Y to select from the list of genre, or press N to have a random book\n")
            if user_genre_choice.lower() == "y":
                while True:
                    display_genre_list()
                    user_2nd_genre_choice = input("Please enter the number for the genre you prefer?\n")
                    if user_2nd_genre_choice.isdigit():
                        get_book_by_genre(user_2nd_genre_choice)
                        break
                    else:
                        print("Invalid input, please try again. Please only enter the number.")
                        continue  # Prompt user to try again

            elif user_genre_choice.lower() == "n":
                get_random_book()
            else:
                print("Invalid input, please try again.")
                continue  # Prompt user to try again

        elif user_choice == "2":
            user_book_id = input("Please enter the book ID you're looking for? (Please enter a number between 1 to 107)\n")
            if int(user_book_id) <= 107:
                get_book_by_id(user_book_id)
            else:
                print("Invalid input, please try again.")
                continue

        elif user_choice == "3":
            user_book_review_id = input("Please enter the book ID you would like to add a review for? (Please enter a number between 1 to 107)\n")
            if user_book_review_id.isdigit() and int(user_book_review_id) <= 107:
                user_review = input("Please enter your review message here:\n")
                add_book_review(user_book_review_id, user_review)
            else:
                print("Invalid input, please try again.")
                continue

        else:
            print("Invalid input, please try again.")
            continue

        while True:
            user_2nd_choice = input(
                "Would you like to continue?\nPress Y to continue, or press N to exit the session.\n")

            if user_2nd_choice.lower() == "y":
                break
            elif user_2nd_choice.lower() == "n":
                print(end_session_graph)  # call the end session graph when the session has ended
                return
            else:
                print("Invalid input, please try again")


# starting with
print("\033[32mHello, and welcome to the Novel Navigators!\033[0m\nDon't know what to read? We got you covered!\n")
print("                 \033[42m  ✮.HERE YOU CAN.....✮  \033[0m          ")
print('''
+--------------------------------------------------------------+
|             ❤ Get a random book recommendation               |
|             ❤ Look up a book by Book ID                      |
|             ❤ Add a book review                              |
|          __...--~~~~~-._   _.-~~~~~--...__                   |
|        //               `V'               \\\\                 |
|       //                 |                 \\\\                |
|      //__...--~~~~~~-._  |  _.-~~~~~~--...__\\\\               |
|     //__.....----~~~~._\\ | /_.~~~~----.....__\\\\              |
|    ====================\\\\|//====================             |
|                        `---`                                 |
+--------------------------------------------------------------+
''')

run()
