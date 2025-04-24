class Book:
    def __init__(self, title: str, author: str, year: str) -> None:
        self.title = title
        self.author = author
        self.year = year


class Library:
    def __init__(self) -> None:
        self.books = []
        self.borrow_books = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, book_title: str) -> bool:
        for i, book in enumerate(self.books):
            if book.title == book_title:
                del self.books[i]
                return True

    def borrow_book(self, book_title: str) -> bool:
        for i, book in enumerate(self.books):
            if book.title == book_title:
                self.borrow_books.append(self.books.pop(i))
                return True

    def return_book(self, book_title: str) -> bool:
        for i, book in enumerate(self.borrow_books):
            if book.title == book_title:
                self.books.append(self.borrow_books.pop(i))
                return True

    def available_books(self) -> list[Book]:
        return [book.title for book in self.books]

    def borrowed_books(self) -> list[Book]:
        return [book.title for book in self.borrow_books]


def show():
    print("Livres en stock:")
    print(lib.available_books())
    print("Livres empruntés:")
    print(lib.borrowed_books())


livres = [
    Book("Les fleurs du mal", "Baudelaire", "1850"),
    Book("La lenteur", "Kundera", "1993"),
    Book("Don quichotte", "Cervantes", "1605"),
]

lib = Library()

print("\nAjout des trois lives")
for livre in livres:
    lib.add_book(livre)
show()

print("\nSupression du livre 'Don quichotte'")
lib.remove_book("Don quichotte")
show()

print("\nEnprunt de 'La lenteur':")
lib.borrow_book("La lenteur")
show()

print("\nRetour de 'La lenteur'")
lib.return_book("La lenteur")
show()
