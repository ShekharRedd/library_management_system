import json

def add_books_to_file(filename, new_books):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            existing_books = data.get("books", [])
            print("Existing books:", existing_books)
    except FileNotFoundError:
        data = {"books": []}
        existing_books = data.get("books", [])
        print("No existing books found.")
    except json.JSONDecodeError:
        data = {"books": []}
        existing_books = data.get("books", [])
        print("Error decoding JSON. Initializing empty list.")

    book_exists = False
    # Check if the book already exists in the list
    for book in existing_books:
        print("books are",book)

    # If book does not exist, add it to the list
    # if not book_exists:
    #     existing_books.append(new_books)  # Append the entire new_books list
    #     data["books"] = existing_books

    #     # Write the updated data to the file
    #     with open(filename, 'w') as file:
    #         json.dump(data, file, indent=3)
    #     print("Book added successfully.")
    # else:
    #     print("Book already exists.")

# Example usage:
new_books = [
    {
        "title": "awd",
        "author": "awd",
        "isbn": "1212"
    }
]
add_books_to_file("data.txt", new_books)
