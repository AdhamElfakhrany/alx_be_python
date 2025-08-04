class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

    def check_out(self):
        self.is_checked_out = True

    def return_book(self):
        self.is_checked_out = False

    def is_available(self):
        return not self.is_checked_out
    
    class Library:
        def __init__(self):
            self._books = []

        def add_book(self, book):
            self.books.append(book)

        def check_out_book(self, title):
            for book in self.books:
                if book.title == title and book.is_available():
                    book.check_out()
                    print(f"{title} is found")
                else:
                    print(f"{title} is not found")
                return
            
        def return_book(self, title):
            for book in self.books:
                if book.title == title and not book.is_available():
                    book.return_book()
                return
        def list_available_books(self):
            for book in self.books:
                if book.is_available():
                    print(f"{book.title} by {book.author}")
