import os
import json

class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn

    def to_dict(self):
        return {
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'isbn': self.isbn
        }

    @staticmethod
    def from_dict(data):
        return Book(data['title'], data['author'], data['year'], data['isbn'])


class Library:
    def __init__(self, file_name='library.json'):
        self.books = []
        self.file_name = file_name
        self.load_books()

    def add_book(self, book):
        self.books.append(book)
        self.save_books()
        print(f"Book '{book.title}' added to the library.")

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for i, book in enumerate(self.books, start=1):
                print(f"{i}. {book.title} by {book.author} ({book.year}) [ISBN: {book.isbn}]")

    def search_books(self, title):
        results = [book for book in self.books if title.lower() in book.title.lower()]
        if results:
            print(f"Found {len(results)} book(s) matching '{title}':")
            for book in results:
                print(f"{book.title} by {book.author} ({book.year}) [ISBN: {book.isbn}]")
        else:
            print(f"No books found with title containing '{title}'.")

    def delete_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                self.save_books()
                print(f"Book '{book.title}' deleted.")
                return
        print(f"No book found with ISBN '{isbn}'.")

    def save_books(self):
        """Save the current list of books to a file."""
        with open(self.file_name, 'w') as file:
            json.dump([book.to_dict() for book in self.books], file, indent=4)
        print("Library saved to file.")

    def load_books(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as file:
                books_data = json.load(file)
                self.books = [Book.from_dict(data) for data in books_data]
            print("Library loaded from file.")
        else:
            print("No existing library file found. Starting with an empty library.")


class BookManagerApp:
    def __init__(self):
        self.library = Library()

    def display_menu(self):
        print("\n--- Book Management System ---")
        print("1. Add a new book")
        print("2. List all books")
        print("3. Search for a book by title")
        print("4. Delete a book by ISBN")
        print("5. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Choose an option: ")
            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.library.list_books()
            elif choice == '3':
                self.search_books()
            elif choice == '4':
                self.delete_book()
            elif choice == '5':
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author: ")
        year = input("Enter publication year: ")
        isbn = input("Enter ISBN: ")
        book = Book(title, author, year, isbn)
        self.library.add_book(book)

    def search_books(self):
        title = input("Enter title to search for: ")
        self.library.search_books(title)

    def delete_book(self):
        isbn = input("Enter ISBN of the book to delete: ")
        self.library.delete_book(isbn)


if __name__ == "__main__":
    app = BookManagerApp()
    app.run()
