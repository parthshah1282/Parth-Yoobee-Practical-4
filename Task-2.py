class book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
class Library:
    def __init__(self):
        self.books = []
    def add_book(self,book):
        self.books.append(book)
        print(f"Book '{book.title}' by {book.author} added successfully.")
    def show_book(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("\nBooks in the library:")
            for idx, book in enumerate(self.books,start=1):
                print(f"{idx}. {book.title} by {book.author}")
def main():
    library = Library()
    while True:
        print("\n==== Library Menu ====")
        print("1. Add Books")
        print("2. Show Books")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            new_book = book(title,author)
            library.add_book(new_book)
        elif choice == '2':
            library.show_book()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
main()

