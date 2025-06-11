class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute

    def __str__(self):
        return f'"{self.title}" by {self.author}'

class Library:
    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        if not isinstance(book, Book):
            print("Error: Only Book objects can be added to the library.")
            return
        self._books.append(book)
        print(f"Added: {book}")

    def check_out_book(self, title):
        found = False
        for book in self._books:
            if book.title == title:
                found = True
                if not book._is_checked_out:
                    book._is_checked_out = True
                    print(f"Checked out: {book.title}")
                else:
                    print(f"'{book.title}' is already checked out.")
                return
        if not found:
            print(f"Book with title '{title}' not found in the library.")

    def return_book(self):
        found = False
        for book in self._books:
            if book.title == title:
                found = True
                if book._is_checked_out:
                    book._is_checked_out = False
                    print(f"Returned: {book.title}")
                else:
                    print(f"'{book.title}' was not checked out.")
                return
        if not found:
            print(f"Book with title '{title}' not found in the library.")

    def list_available_books(self):
        available_count = 0
        for book in self._books:
            if not book._is_checked_out:
                print(f"- {book.title} by {book.author}")
                available_count += 1
        if available_count == 0:
            print("No books available.")
