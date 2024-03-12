import json
import datetime

class Storage_User:
    filename="data.txt"
    def __init__(self):
        pass

    def add_user_to_file(self,name, user_id):
        # Read existing user data from the file
        try:
            with open('data.txt', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {"users": []}

        # Check if the user already exists
        existing_users = data.get("users", [])
        user_exists = any(user["user_id"] == user_id for user in existing_users)

        if not user_exists:
            # Add the new user to the list
            new_user = {"name": name, "user_id": user_id}
            existing_users.append(new_user)
            data["users"] = existing_users
            # Write the updated user data to the file
            with open('data.txt', 'w') as file:
                json.dump(data, file, indent=4)
                print("User added successfully.")
                return True
        else:
            print("User already exists.")
            return False

    def list_users(self):
        try:
            with open(Storage_Books.filename,"r") as file:
                users=json.load(file)
                return users["users"]
        except Exception as ex:
            return None 
    def delete_users(self, user_id):
            print("welcome")
            try:
                with open(Storage_Books.filename,"r") as file:
                    data=json.load(file)
                    delete_user=data.get("users",[])
            except Exception as ex:
                print("please try again")
            
            update_user =[user for user in delete_user if user["user_id"]!=user_id]
            data["users"]=update_user
            try :
                with open(Storage_User.filename,"w") as filename:
                    json.dump(data,filename,indent=3)
                    return True
            except Exception as ex: 
                print("Please try again ")

class Storage_Books:
    filename="data.txt"
    def __init__(self) -> None:
        pass

    @staticmethod    
    def get_books_details(filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                existing_books = data.get("books", [])
                print("Existing books:", existing_books)

                return existing_books,data
                
        except FileNotFoundError:
            data = {"books": []}
            existing_books = data.get("books", [])
            print("No existing books found.")
            return existing_books,data
            
        except json.JSONDecodeError:
            data = {"books": []}
            existing_books = data.get("books", [])
            print("Error decoding JSON. Initializing empty list.")
            return existing_books, data
            

    def add_books_to_file(self, filename, new_books):
        existing_books,data=self.get_books_details(filename)
        book_exists = False
        # Check if the book already exists in the list
        for book in existing_books:
            if book["isbn"] == new_books[0]["isbn"]:
                book_exists = True
                break

        # If book does not exist, add it to the list
        if not book_exists:
            existing_books.append(new_books[0])
            data["books"] = existing_books

            # Write the updated data to the file
            with open(filename, 'w') as file:
                json.dump(data, file, indent=3)
            print("Book added successfully.")
        else:
            print("Book already exists.")

    def list_books_from_file(self,filename):
        existing_book,data=self.get_books_details(filename)
        return existing_book
    
    def update_book(self, isbn):
        existing_books, data = self.get_books_details(Storage_Books.filename)
        check_in=data.get("check-in",[])
        # print("helllo",existing_books)
        # print("hi",data)
        found = False
        for book in existing_books:
            if book["isbn"] == isbn:
                bk = input("Enter the new title: ")
                au = input("Enter the new author: ")
                book["title"] = bk
                book["author"] = au
                # print("Updated book details:", book)
                found = True
                break

        if found:
            for chk_book in check_in:
                if chk_book["isbn"] == isbn:
                    chk_book["title"] = bk
                    chk_book["author"] = au

            # Write the updated data back to the file
            with open(Storage_Books.filename, 'w') as file:
                json.dump(data, file, indent=3)
            return "Book details updated successfully."
        else:
            return "No book found with the provided ISBN."
    
    def search_book(self,isbn):
        existing_books, data = self.get_books_details(Storage_Books.filename)
        search=False
        book_item=None
        for book in existing_books:
            if book["isbn"] == isbn:
                search=True
                book_item=book
                break
                
        if search:
            return book
        else:
            return None

    # def delete_book(self, isbn):
    #     try:
    #         with open(Storage_Books.filename, "r") as filename:
    #             data = json.load(filename)
    #             check_in = data.get("check-in", [])
    #             delete_bk = data.get("books", [])
    #     except Exception as ex:
    #         print("Invalid request:", ex)
    #         return False
    #     print("data",delete_bk)
    #     found_index = None
    #     print("before")
    #     for i, book in enumerate(delete_bk):
    #         if book["isbn"] == isbn:
    #             print(book["isbn"])
    #             print(i)
    #             found_index = i
    #             print("after it",i)
    #             break
    #     print("after")
    #     print(found_index)
    #     if found_index is not None:
    #         print("inside")
    #         delete_bk.pop(found_index)
    #         check_in.pop(found_index)
    #         print("found index")
    #         try:
    #             with open(Storage_Books.filename, "w") as filename:
    #                 json.dump(data, filename, indent=3)
    #             print("Book deleted successfully.")
    #             return True
    #         except Exception as ex:
    #             print("Error writing to file:", ex)
    #             return False
    #     else:
    #         print("Book with ISBN", isbn, "not found.")
    #         return False

    
    def delete_book(self, isbn):
        try:
            with open(Storage_Books.filename, "r") as filename:
                data = json.load(filename)
                check_in = data.get("check-in", [])
                books = data.get("books", [])
        except Exception as ex:
            print("Invalid request:", ex)
            return False
            
        print("Books to delete:", books)  # Print the contents of the books list
            
        # Find the index of the book with the given ISBN in both lists
        book_index = None
        for i, book in enumerate(books):
            if book["isbn"] == isbn:
                book_index = i
                break

        if book_index is not None:
            # Remove the book from the books list
            deleted_book = books.pop(book_index)
            
            # Remove the corresponding entry from the check-in list
            if book_index < len(check_in):
                check_in.pop(book_index)
            
            # Update the data dictionary with the modified lists
            data["books"] = books
            data["check-in"] = check_in

            try:
                with open(Storage_Books.filename, "w") as filename:
                    json.dump(data, filename, indent=3)
                print("Book deleted successfully.")
                # Log the operatio
                return True
            except Exception as ex:
                print("Error writing to file:", ex)
                return False
        else:
            print("Book with ISBN", isbn, "not found.")
            return False


                


class Storage_Check_In:
    filename="data.txt"
    def __init__(self) -> None:
        pass
    def check_in(self,isbn): # means availabe to borrow 
        try :
            with open(Storage_Check_In.filename,"r") as filename:
                data=json.load(filename)
                all_books=data.get("books",[])
                check_in=data.get("check-in",[])
                check_out=data.get("check-out",[])
        except Exception as ex:
            print("cannot read the file") 

        for i, book in enumerate(check_out):
            if book["isbn"] == isbn:
                # Remove the book from check-out
                returned_book = check_out.pop(i)
                # Add the book to check-in
                check_in.append(returned_book)
                
                try:
                    with open(Storage_Check_In.filename, "w") as file:
                        json.dump(data, file, indent=4)
                    print("Your book has been checked in.")
                    print("Thank you for returning it.")
                    return True
                except Exception as ex:
                    print("Error writing to file:", ex)
                    return False
                break  # Exit the loop once the book is found and processed
        else:
            print("Book with ISBN", isbn, "not found in check-out.")
            return False



class Add_Book_Checkin:
    filename = "data.txt"
    
    def __init__(self):
        pass 

    def add_checkin(self, isbn):
        try:
            with open(Add_Book_Checkin.filename, "r") as file:
                data = json.load(file)
                total_books = data.get("books", [])
        except Exception as ex:
            print("Invalid file:", ex)
            return False
        
        found_book = None
        for book in total_books:
            if book["isbn"] == isbn:
                found_book = book
                break
        
        if found_book:
            try:
                with open(Add_Book_Checkin.filename, "w") as file:  # Open in write mode to update the file
                    data["check-in"].append(found_book.copy())  # Append a copy of the found book
                    json.dump(data, file, indent=2)  # Write the updated data to the file
                return True
            except Exception as ex:
                print("Error writing to file:", ex)
                return False
        else:
            print("Please check the ISBN to add check-in.")
            return False





class Storage_Check_Out:
    filename = "data.txt"
    def __init__(self) -> None:
        pass
    
    def check_out_book_list(self, isbn):
        try:
            with open(Storage_Check_Out.filename, "r") as file:
                data = json.load(file)
                all_books = data.get("books", [])
                check_in = data.get("check-in", [])
                check_out = data.get("check-out", [])
        except Exception as ex:
            print("Error reading file:", ex)
            return False

        check_all_book = [book for book in all_books if book["isbn"] == isbn]
        
        if check_all_book:
            # Find the book in the check-in list
            check_out_book = next((book for book in check_in if book["isbn"] == isbn), None)
            
            if check_out_book:
                print("Book is available. Please take it.")
                # Move the book from check-in to check-out
                check_out.append(check_out_book)
                check_in.remove(check_out_book)

                try:
                    with open(Storage_Check_Out.filename, "w") as file:
                        json.dump(data, file, indent=2)
                    return True
                except Exception as ex:
                    print("Error writing to file:", ex)
                    return False
            else:
                print("Book is not available. Please check-in list or Already borrowed.")
                return False
        else:
            print("Invalid book.")
            return False

        

class Track_Book:

    filename = "data.txt"

    def __init__(self):
        pass
    
    def track_book_availability(self, isbn):
        try:
            with open(Track_Book.filename, "r") as file:
                data = json.load(file)
                all_books = data.get("books", [])
                check_in = data.get("check-in", [])
                check_out = data.get("check-out", [])
        except Exception as ex:
            print("Error reading file:", ex)
            return False
        
        for book in all_books:
            if book["isbn"] == isbn:
                if book in check_in:
                    print("Book with ISBN", isbn, "is available for borrowing.")
                    return True
                elif book in check_out:
                    print("Book with ISBN", isbn, "is currently checked out.")
                    return False
                else:
                    print("Book with ISBN", isbn, "is not listed for borrowing or checked out.")
                    return False
        
        print("Book with ISBN", isbn, "not found in the library.")
        return False
    def log_operation(self, operation):
        try:
            with open("log.txt", "a") as file:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"{timestamp}: {operation}\n")
            # print("Operation logged successfully.")
        except Exception as ex:
            print("Error logging operation:", ex)
        




