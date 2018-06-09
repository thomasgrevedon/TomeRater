class User(object):
    def __init__(self, name, email):
        self.name = name #this will be a string
        self.email = email #this will be a string
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
        if other_user.name == self.name:
            return other_user.email == self.email

    def read_book(self, book, rating = "None"):
        self.books[book] = rating

    def get_average_rating(self):
        total = 0
        for i in self.books.values():
            total += i
        if len(self.books.values()) > 0:
            average = total / len(self.books.values())
            return average



class Book(object):
    def __init__(self, title, isbn):
        self.title = title #this will be a string
        self.isbn = isbn #this will be a number
        self.rating = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("the book's ISBN has been updated")

    def add_rating(self, rating):
        if rating >= 0 and rating <= 4:
            self.rating.append(rating)
        else:
            print("invalid Rating")

    def __eq__(self, other_book):
        if other_book.title == self.title:
            return other_book.isbn == self.isbn

    def get_average_rating(self):
        total = 0
        for i in self.rating:
            total += i
        if len(self.rating) > 0:
            average = total / len(self.rating)
            return average

    def __hash__(self):
        return hash((self.title, self.isbn))


class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title = self.title, author = self.author)

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject #this will be a string
        self.level = level #this will be a string

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject)

class TomeRater(object):
    def __init__(self):
        self.users = {} #this will map a user's email to the cooresponding User obeject
        self.books = {} #this will map a Book object to the number of Users that have read it

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating = "None"):
        try:
            self.users[email]
            self.users[email].read_book(book, rating)
            if rating != "None":
                book.add_rating(rating)
            try:
                self.books[book]
                self.books[book] += 1
            except KeyError:
                self.books[book] = 1
        except KeyError:
            print("No user with email {email}".format(email = email))

    def add_user(self, name, email, books = "None"):
        self.users[email] = User(name, email) #should I ass self?
        if books != "None":
            for i in books:
                self.add_book_to_user(i, email)


Tome_Rater = TomeRater()
Tome_Rater.add_user("Thomas", "thomas.grevedon@gmail.com", books = ["oui", "le meilleur du jeu"])
print(Tome_Rater.users)
print(Tome_Rater.books)
