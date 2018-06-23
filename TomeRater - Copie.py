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
        average = 0
        for i in self.books:
            if self.books[i] != "None":
                total += self.books[i]
            else:
                continue
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
        average = 0
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

    def add_user(self, name, email, user_books = "None"):
        self.users[email] = User(name, email) #adds the email as Key in dictionnary of the class and add the User class as value
        if user_books != "None":
            for i in user_books:
                self.add_book_to_user(i, email)

    def print_catalog(self):
        for i in self.books.keys():
            print(i.title)

    def print_users(self):
        for i in self.users.values():
            print(i)

    def get_most_read_book(self):
        total = 0
        most_read_book = ""
        for i in self.books:
            if self.books[i] > total:
                most_read_book = i.title
                total = self.books[i]
        return most_read_book

    def highest_rated_book(self):
        highest_average = 0
        highest_rated_book = ""
        for i in self.books:
            average_rating = i.get_average_rating()
            if average_rating > highest_average:
                highest_average = average_rating
                highest_rated_book = i.title
        return highest_rated_book

    def most_positive_user(self):
        highest_average = 0
        highest_positive_user = ""
        for i in self.users.values():
            average_rating = i.get_average_rating()
            if average_rating > highest_average:
                highest_average = average_rating
                highest_positive_user = i
        return highest_positive_user

"""
Tome_Rater = TomeRater()
book1 = Tome_Rater.create_book("le meilleur des mondes", 3456)
book2 = Tome_Rater.create_book("le meilleur du jeu", 32673838456)
bookbook = Tome_Rater.create_book("bookbook", 345566)
bookbookbof = Tome_Rater.create_book("bookbookbof", 348756)
print(book1)
Tome_Rater.add_user("Thomas", "thomas.grevedon@gmail.com", user_books = [book1])
Tome_Rater.add_user("Thoma", "thomas.greveon@gmail.com", [book1])
Tome_Rater.add_user("Tho", "thomas.@gmail.com", [book2])
print(Tome_Rater.books)
Tome_Rater.print_catalog()
Tome_Rater.print_users()
print(Tome_Rater.get_most_read_book())
Tome_Rater.add_book_to_user(bookbook, "thomas.grevedon@gmail.com", 4)
Tome_Rater.add_book_to_user(bookbook, "thomas.greveon@gmail.com", 2)
Tome_Rater.add_book_to_user(bookbookbof, "thomas.grevedon@gmail.com", 2)
Tome_Rater.add_book_to_user(bookbookbof, "thomas.@gmail.com", 2)
print(Tome_Rater.highest_rated_book())
print(Tome_Rater.most_positive_user())
"""

"""
ideas
add commments of book in string in string
"""
