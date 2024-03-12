# book.py
# from models import Book

# books = []

# def add_book(title, author, isbn):
#     book = Book(title, author, isbn)
#     books.append(book)


# book.py

from models import Book

from storage import Storage_User, Storage_Books

st=Storage_Books()
filename="data.txt"


class BookManagement:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, isbn):
        data = [{
            "title": title,
            "author": author,
            "isbn": isbn
        }]
        print(data)
        try:
            
            st.add_books_to_file(filename,data )
        except Exception as ex:
            print("Exception in book file:", ex)
            return ex

    def list_books(self):
        print("Welcome")
        books = st.list_books_from_file(filename)
        for book in books:
            print(book)
    def update_books(self,isbn):
        update_bk=st.update_book(isbn)
        # print(update_bk)
        if update_bk :
            print(update_bk)
        else:
            print(update_bk)

    def delete_books(self,isbn):
        print("welcome to")
        delete_bk =st.delete_book(isbn)
        print("sdffsd")
        if delete_bk :
            print("Successfully deleted ")
            return True
        else :
            print("please try again sdhjbebhj")
            return False

    def search_books(self,isbn):
        search_bk=st.search_book(isbn)
        if search_bk :
            print("Book Exist  :",search_bk)
        else :
            print("No books exist")


        
