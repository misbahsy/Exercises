import json
book_author_list = {
    "books": {
        "book_a": "author_a",
        "book_b": "author_b",
        "book_c": "author_c",
    }
}

book_list = json.dumps(book_author_list)

def get_list():
    return book_list

def retrive_book(book):
    data = json.loads(book_list)
    books = data["books"]
    result = books.get(book)

    return result