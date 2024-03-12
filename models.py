# models.py
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.isbn}')"

class User:
    def __init__(self, username, user_id):
        self.username = username
        self.user_id = user_id

    def __repr__(self):
        return f"User('{self.username}', '{self.user_id}')"

