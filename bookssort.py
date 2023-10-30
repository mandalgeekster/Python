class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN

def bubble_sort_books(book_list, key):
    n = len(book_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if key(book_list[j]) > key(book_list[j+1]):
                book_list[j], book_list[j+1] = book_list[j+1], book_list[j]

def display_books(book_list):
    for book in book_list:
        print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.ISBN}")

def main():
    library = []

    # Adding books to the library
    library.append(Book("Book To Kill a Mockingbird", "Author Harper Lee ", "ISBN3"))
    library.append(Book("Book 1984", "Author George Orwell", "ISBN1"))
    library.append(Book("Book Pride and Prejudice", "Author Jane Austen", "ISBN2"))
    library.append(Book("Book The Great Gatsby", "Author  F. Scott Fitzgerald", "ISBN6"))
    library.append(Book("Book The Catcher in the Rye", "Author  J.D. Salinger", "ISBN4"))
    library.append(Book("Book Moby-Dick", "Author Herman Melville", "ISBN5"))
    library.append(Book("Book  by Herman MelvilleWar and Peace", "Author Leo Tolstoy", "ISBN7"))

    print("Books in the library (unsorted):")
    display_books(library)

    # Sort by Title
    bubble_sort_books(library, key=lambda book: book.title)
    print("\nBooks in the library (sorted by title):")
    display_books(library)

    # Sort by ISBN
    bubble_sort_books(library, key=lambda book: book.ISBN)
    print("\nBooks in the library (sorted by ISBN):")
    display_books(library)

    # Sort by Author
    bubble_sort_books(library, key=lambda book: book.author)
    print("\nBooks in the library (sorted by Author):")
    display_books(library)

if __name__ == "__main__":
    main()
