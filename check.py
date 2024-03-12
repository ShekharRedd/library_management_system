
import json


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
