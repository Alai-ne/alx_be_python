 from book_class import Book

# Create an instance of the Book class
book1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979)

# Use the string representation method
print(str(book1))

# Use the official representation method
print(repr(book1))

# Delete the object to trigger the destructor
del book1from book_class import Book

# Create an instance of the Book class
book1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979)

# Use the string representation method
print(str(book1))

# Use the official representation method
print(repr(book1))

# Delete the object to trigger the destructor
del book1


from library_system import Library, EBook, PrintBook

# Create a library instance
my_library = Library()

# Create book instances
book1 = EBook("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1500)
book2 = PrintBook("Dune", "Frank Herbert", 800)
book3 = Book("1984", "George Orwell")

# Add books to the library
my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)

# List all books in the library
my_library.list_books()


from class_static_methods_demo import Calculator

def main():
    # Using the static method
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # Using the class method
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")

