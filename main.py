from book import BookManagement
from user import UserManagement
from storage import Storage_Check_In, Storage_Check_Out, Add_Book_Checkin, Track_Book

book_management = BookManagement()
user_management = UserManagement()
sci = Storage_Check_In()
sco = Storage_Check_Out()
ab = Add_Book_Checkin()
tb = Track_Book()

def main_menu():
    print("\nLibrary Management System")
    print("1. User Management")
    print("2. Book Management")
    print("3. Tracking")
    print("4. Checkout Book")
    print("5. Check-in Book")
    print("6. Admin: Add book to check-in list")
    print("7. Exit")
    choice = input("Enter choice: ")
    return choice

def user_menu():
    print("\nUser Management")
    print("1. Add User")
    print("2. List Users")
    print("3. Delete User")
    print("4. Back to Main Menu")

def book_menu():
    print("\nBook Management")
    print("1. Add Book")
    print("2. List Books")
    print("3. Delete Book")
    print("4. search Books")
    print("5. Update Book")
    print("6. Back to Main Menu")

def tracking_menu():
    print("\nTracking")
    print("1. Track Book Availability")
    print("2. Back to Main Menu")

def main():
    while True:
        choice = main_menu()
        tb.log_operation(f"{choice} Main Page")
        if choice == '1':
            while True:
                user_menu()
                sub_choice = input("Enter choice: ")
                tb.log_operation(f"{sub_choice} User Management")
                if sub_choice == '1':
                    try:
                        name = input("Enter user name: ")
                        user_id = int(input("Enter user ID: "))
                        user_management.add_user(name, user_id)
                        # print("User added.")
                    except Exception as ex:
                        print("Invalid please enter the user_id : ")

                elif sub_choice == '2':
                    try:
                        user_management.list_user()
                    except Exception as ex:
                        print("Please try again.")
                elif sub_choice == '3':
                    du = int(input("Enter the user ID to delete: "))
                    try:
                        user_management.delete_user(du)
                    except Exception as ex:
                        print("Please try again.")
                elif sub_choice == '4':
                    break
                else:
                    print("Invalid choice, please try again.")
        elif choice == '2':
            while True:
                book_menu()
                sub_choice = input("Enter choice: ")
                tb.log_operation(f"{sub_choice} Book Management")
                if sub_choice == '1':
                    while True:
                        title = input("Enter title: ")
                        author = input("Enter author: ")
                        isbn_input = input("Enter ISBN (enter 'exit' to cancel): ")

                        if isbn_input.lower() == 'exit':
                            print("Exiting book addition process.")
                            break
                        
                        try:
                            isbn = int(isbn_input)
                            book_management.add_book(title, author, isbn)
                            print("Book added successfully.")
                            break
                        except ValueError:
                            print("Invalid input! Please enter a valid integer for the ISBN.")


                elif sub_choice == '2':
                    
                    book_management.list_books()
                elif sub_choice == '3':
                    isbn = int(input("Enter the ISBN of the book to delete: "))
                    try:
                        book_management.delete_books(isbn)
                    except Exception as ex:
                        print("Please try one more time.")

                elif sub_choice =="4":
                    isbn = int(input("Enter the ISBN of the book to search: "))
                    book_management.search_books(isbn)
                elif sub_choice=="5":
                    isbn=int(input("Enter the ISBN Number to Update"))
                    book_management.update_books(isbn)

                elif sub_choice == '6':
                    break
                else:
                    print("Invalid choice, please try again.")
        elif choice == '3':
            
            while True:
                tracking_menu()
                sub_choice = input("Enter choice: ")
                tb.log_operation(f"{sub_choice} Tracking Management")
                if sub_choice == '1':

                    
                    try:
                        isbn = int(input("Please enter the ISBN number to track the book availability: "))
                        tb.track_book_availability(isbn)
                    except Exception as ex:
                        print("Please enter the correct ISBN.")
                elif sub_choice == '2':
                    break
                else:
                    print("Invalid choice, please try again.")
        elif choice == '4':
            tb.log_operation(f"{choice} Checkout Management ")
            isbn=int(input("Enter the isbn numerb to borrow : "))
            sco.check_out(isbn)
        elif choice == '5':
            tb.log_operation(f"{choice} Checkin Management ")
            isbn=int(input("Enter the isbn numerb to check-in : "))
            sci.check_in(isbn)
        elif choice =="6":
            tb.log_operation(f"{choice} Admin add checkin list  Management ")
            isbn=int(input("Enter the isbn numerb to check-in : "))
            ab.add_checkin(isbn)
        elif choice == '7':
            print("Exiting.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
