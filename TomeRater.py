class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {} #this will map a book object


    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("User's email has been updated")

    def __repr__(self):
        number_of_books_red = len(self.books)
        return "User {user}, email {email}, books read: {books_red}".format(user = self.name, email = self.email, books_red = number_of_books_red)

    def __eq__(self, other_user):
        pass

user1 = User("Stephen Hawking", "hawking@universe.edu")
print(user1)
user1.change_email("ouiouioui")
user1.books = {"lala": "ok", "lol": "not ok"}
print(user1)
