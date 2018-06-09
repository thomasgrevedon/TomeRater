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
        return other_user.name == self.name
        return other_user.email == self.email


user1 = User("Thomas", "thomas.grevedon@gmail.com")
user2 = User("Thoma", "thomas.grevedon@gmail.com")
print(user1 == user2)
