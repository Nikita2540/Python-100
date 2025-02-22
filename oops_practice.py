class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._available = True

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        raise ValueError("Title cannot be modified")
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        raise ValueError("Author cannot be modified")

    def is_available(self):
        if self._available:
            return 'Available'
        else:
            return 'Unavailable'
    def bookinfo(self):
        return f"title: {self.title}, author: {self.author}"
    def borrow_book(self):
        if self._available:
            self._available = False
            return f"You borrowed '{self.title}'"
        else:
            return f"The book '{self.title}' is unavailable"
    def return_book(self):
        if not self._available:
            self._available = True
            return f"You returned '{self.title}'"
        else:
            return f"'{self.title}' was never borrowed"

book_1 = Book('And then there were none', 'Agatha Crishtie')

print(book_1.is_available())
print(book_1.borrow_book())
print(book_1.is_available())
print(book_1.return_book())
print(book_1.is_available())