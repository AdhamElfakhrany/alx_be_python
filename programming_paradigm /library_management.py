class Book:
    """
    Represent a book with its attributes
    """
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    """
    Represent the library that holds books
    """
    def __init__(self):
        self._books = []
    
    def add_book(self,book):
        self._books.append(book)
    
    def check_out_book(self,title):
        for book in self._books:
            if title == book.title:
                if book.check_out():
                    # print(f"Checked out {book.title}.")
                    return True
                else:
                    # print("Book isn't available at the moment.")
                    return False
        print(f"{title} was Not Found.")
    
    def return_book(self,title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    # print(f"Returned {book.title}.")
                    return True
                else:
                    # print(f"{book.title} Isn't checkedout yet.")
                    return False
        print(f"{title} was Not Found.")
    
    def list_available_books(self):
        for book in self._books:
            if not book._is_checked_out:
                print(book)
                

        


    
