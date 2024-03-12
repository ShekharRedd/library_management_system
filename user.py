# from models import User

# users = []

# def add_user(name, user_id):
#     user = User(name, user_id)
#     users.append(user)


# user.py
from models import User
from storage import Storage_User

sb=Storage_User()


class UserManagement:
    def __init__(self):
        self.users = []

    def add_user(self, username, user_id):
        user = sb.add_user_to_file(username,user_id)
        if user:
            print("user is added")
        else:
            pass
    def list_user(self):
        user_update=sb.list_users()
        if user_update:
            print("All users are : ",user_update)
        else:
            print("No user exists")


    def delete_user(self,user_id):
        user_delete=sb.delete_users(user_id)
        if user_delete:
            print("User deleted successfully")
        else :
            print("Invalid request")
            
