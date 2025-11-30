import sys
from robust_division_calculator import safe_divide

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
    else:
        numerator_input = sys.argv[1]
        denominator_input = sys.argv[2]
        result = safe_divide(numerator_input, denominator_input)
        print(f"Result: {result}")


        from library_management import Book, Library

def main():
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("Available books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Simulate returning a book
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()
