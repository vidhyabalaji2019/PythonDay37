# Library Book Management System

# Nested dictionary to store books
library = {
    "Book001": {"title": "Python Programming", "author": "Guido van Rossum", "copies": 5},
    "Book002": {"title": "Data Science Essentials", "author": "Andrew Ng", "copies": 3},
}

# Function to add a new book
def add_book(book_id, title, author, copies):
    if book_id in library:
        print(f"{book_id} already exists in the library.")
    else:
        library[book_id] = {"title": title, "author": author, "copies": copies}
        print(f"Book '{title}' added successfully!")

# Function to update book availability
def update_book(book_id, copies_change):
    if book_id in library:
        library[book_id]["copies"] += copies_change
        if library[book_id]["copies"] < 0:
            library[book_id]["copies"] = 0
        print(f"Book '{library[book_id]['title']}' updated successfully!")
    else:
        print(f"{book_id} not found in the library.")

# Function to remove a book
def remove_book(book_id):
    if book_id in library:
        removed_title = library[book_id]["title"]
        del library[book_id]
        print(f"Book '{removed_title}' removed from the library.")
    else:
        print(f"{book_id} not found in the library.")

# Function to list all books
def list_books():
    if library:
        print("\n📚 Library Books:")
        for book_id, details in library.items():
            print(f"ID: {book_id}")
            print(f"  Title : {details['title']}")
            print(f"  Author: {details['author']}")
            print(f"  Copies: {details['copies']}")
            print("-" * 30)
    else:
        print("No books in the library.")

# ------------------- Example Usage -------------------
add_book("Book003", "Machine Learning", "Tom Mitchell", 4)
update_book("Book001", -2)  # Borrow 2 copies
update_book("Book002", 1)   # Return 1 copy
remove_book("Book003")
list_books()
