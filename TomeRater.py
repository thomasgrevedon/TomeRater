import weakref

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
    instances = set()

    def __init__(self, title, isbn, price = 0):
        self.title = title #this will be a string
        self.isbn = isbn #this will be a number
        self.instances.add(weakref.ref(self))
        self.rating = []
        self.price = price

    def isIsbnExist(self, isbn):
        if len(Book.instances) > 0:
            isbn_list = []
            for book in Book.instances:
                book = book()
                isbn_list.append(book.isbn)
            return isbn in isbn_list
        else:
            return False

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
    def __init__(self, title, author, isbn, price = 0):
        super().__init__(title, isbn, price)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title = self.title, author = self.author)

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn, price = 0):
        super().__init__(title, isbn, price)
        self.subject = subject #this will be a string
        self.level = level #this will be a string

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject)

class TomeRater(object):
    MessageIsbnAlreadyExists = "Sorry, this ISBN already exists, please choose another ISBN for this book"
    MessageUserAlreadyExists = "This user already exists. Please, choose add_book_to_user function in order to add book to this reader! Thanks mate"

    def __init__(self):
        self.users = {} #this will map a user's email to the cooresponding User obeject
        self.books = {} #this will map a Book object to the number of Users that have read it

    def create_book(self, title, isbn, price = 0):
        if Book.isIsbnExist(self, isbn) == False:
            return Book(title, isbn, price)
        else:
            print(TomeRater.MessageIsbnAlreadyExists)

    def create_novel(self, title, author, isbn, price = 0):
        print("ATTENTION ATTENTION")
        if Book.isIsbnExist(self, isbn) == False:
            print("ah ah je t'a eu")
            print(Book.isIsbnExist(self, isbn))
            return Fiction(title, author, isbn, price)
        else:
            print(TomeRater.MessageIsbnAlreadyExists)

    def create_non_fiction(self, title, subject, level, isbn, price = 0):
        if Book.isIsbnExist(self, isbn) == False:
            return Non_Fiction(title, subject, level, isbn, price)
        else:
            print(TomeRater.MessageIsbnAlreadyExists)

    def add_book_to_user(self, book, email, rating = "None"):
        try:
            self.users[email]
            try:
                book.isbn
                self.users[email].read_book(book, rating)
                if rating != "None":
                    book.add_rating(rating)
                try:
                    self.books[book]
                    self.books[book] += 1
                except KeyError:
                    self.books[book] = 1
            except AttributeError:
                print("sorry the following book \"{book}\" could not be added to the user as it needs to be created first.".format(book = book))
        except KeyError:
            print("No user with email {email}".format(email = email))

    def add_user(self, name, email, user_books = "None"):
        try:
            self.users[email]
            print(TomeRater.MessageUserAlreadyExists)
        except KeyError:
            checkList = ["@", ".edu", '.org', '.com', '.try']
            sensor = 1
            needMessage = True
            while sensor < len(checkList):
                if checkList[0] in email and checkList[sensor] in email:
                    self.users[email] = User(name, email) #adds the email as Key in dictionnary of the class and add the User class as value
                    if user_books != "None":
                        for i in user_books:
                                self.add_book_to_user(i, email)
                    needMessage = False
                    break
                else:
                    sensor += 1
                    continue
            if needMessage == True:
                extension = ""
                for i in checkList[1:]:
                    extension += "\"" + i + "\" "
                print("Please check the email address of user and make sure it has the following characheters: \"@\" and one of the following extension: " + extension)
                #first test "\""
                # for check in checklist message = please check that you have and the following email extension " " + "\"" check +  "\"" + ","
                #print("Please check the email address of user and make sure it has the following characheters: \"@\" and \".edu\" \".com\" \".org\" ")


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

    def get_n_most_read_books(self, n = 0):
        total = 0
        new_dict = dict(self.books)
        ordered_lst = []
        sensor = 1
        if n <= len(new_dict) and n >= sensor:
            while sensor <= n:
                for i in new_dict:
                    if new_dict[i] > total:
                        value = i.title
                        valueToRemove = i
                        total = self.books[i]
                        print(i)
                ordered_lst.append(value)
                new_dict.pop(valueToRemove)
                total = 0
                sensor += 1
            return ordered_lst
        else:
            return "Please choose a number between 1 and {number} both included".format(number = len(new_dict))

    def get_n_most_prolific_user(self, n = 0):
        total = 0
        temp_dic = dict(self.users)
        mostProlificUsers = []
        if n <= len(temp_dic) and len(temp_dic) > 0:
            while len(temp_dic) != 0:
                for user in temp_dic:
                    if len(temp_dic[user].books) > total:
                        value = temp_dic[user]
                        valueToRemove = user
                        total = len(temp_dic[user].books)
                mostProlificUsers.append(value)
                temp_dic.pop(valueToRemove)
                total = 0
            return mostProlificUsers[0: n]
        elif len(temp_dic) == 0:
            return "Your request cannot be processed since no users have been created. Pease create users before calling this request."
        else:
            return 'Your request exceed the number of users in the databse. Please choose a number between 1 and {number} both included'.format(number = len(temp_dic))
        #message for number of users lije the number of books red

    def get_n_most_expensive_books(self, n=4):
        total = -1
        temp_dic = {}
        price_lst = []
        book_name = []
        if len(Book.instances) > 0:
            for book in Book.instances:
                book = book()
                temp_dic[book.title] = book.price
            print(temp_dic)
            while len(temp_dic) != 0:
                for book in temp_dic:
                    #print(temp_dic)
                    if temp_dic[book] > total:
                        title_to_add = book
                        valueToRemove= book
                        price_to_add = temp_dic[book]
                        total = temp_dic[book]
            #            print(total)
                book_name.append(title_to_add)
                price_lst.append(price_to_add)
                temp_dic.pop(valueToRemove)
                total = -1
            nameAndPriceLst = list(zip(book_name, price_lst))
            print(nameAndPriceLst)
            if n <= len(nameAndPriceLst):
                for tuple in range(0, n):
                    sensor = 0
                    book = ""
                    price = 0
                    for item in nameAndPriceLst[tuple]:
                        if sensor == 0:
                            book = item
                            sensor = 1
                        else:
                            price = item
                            sensor = 0
                    print("The book's name is \"{book}\" coming with the following price ${price}".format(book = book, price = price))
                return "End of list"
            else:
                return "Please choose a number between 1 and {n} boh included".format(n = len(nameAndPriceLst))
        else:
            return "The book catalog is empty, please create some books first"

    def get_worth_of_user(self, user_email):
        try:
            self.users[user_email]
            total = 0
            for i in self.users[user_email].books:
                for book in Book.instances:
                    book = book()
                    if book.title == i.title:
                        value = book.price
                        total += value
            return "The sum of all costs of books read by {user} is ${value}".format(user = self.users[user_email].name, value = total)
        except KeyError:
            return "Sorry there is no user with this email address or no email address has been provided. Please check the provided email address"

    def __repr__(self):
        return "The most read book is \'{book_most_red}\' and the highest rated book is \'{book_highest_rated}\'. The most psitive reader is \'{user}\'"\
        .format(book_most_red = self.get_most_read_book(), book_highest_rated = self.highest_rated_book(), user = self.most_positive_user())

Tome_Rater = TomeRater()
Tome_Rater.print_catalog()
print(Tome_Rater.get_n_most_prolific_user(3))
print(Tome_Rater.get_n_most_expensive_books(5))
book1 = Tome_Rater.create_book("le meilleur des mondes", 3456, 20)
book3 = Tome_Rater.create_book("le meilleur des sites", 34567, 15)
book4 = Tome_Rater.create_book("le meilleur des test", 34567, 13)
book5 = Tome_Rater.create_book("le meilleur des sites", 345671, 10)
book6 = Tome_Rater.create_novel("le meilleur des novel", "Bernard De la Villardiere", 3456, 30)
book7 = Tome_Rater.create_non_fiction("le meilleur des website", "Python", "Beginner", 3456, 40)
book8 = Tome_Rater.create_novel("le meilleur des website", "Python", 34567, 12)
book9 = Tome_Rater.create_novel("je fais juste un trst pour voir", "Python", 345674444, 8)
print(book1.title)
Tome_Rater.print_catalog()
print(book3.isbn)
book2 = Tome_Rater.create_book("le meilleur du jeu", 32673838456, 45)
bookbook = Tome_Rater.create_book("bookbook", 345566, 13)
bookbookbof = Tome_Rater.create_book("bookbookbof", 348756, 16)
bookbookbof1 = Tome_Rater.create_book("bookbookbof1", 3487569)
bookbookbof2 = Tome_Rater.create_book("bookbookbof2", 3487568, 21)
bookbookbof3 = Tome_Rater.create_book("bookbookbof3", 3487567, 12)
bookbookbof4 = Tome_Rater.create_book("bookbookbof4", 3487565, 7)
print(book1)
Tome_Rater.add_user("Thomas", "thomas.grevedon@gmail.com", user_books = [book1, "je fais juste un trst pour voir"])
Tome_Rater.add_user("Thomas", "thomas.grevedon@gmail.com", user_books = [book2])
Tome_Rater.add_book_to_user(book2, "thomas.grevedon@gmail.com")
Tome_Rater.add_user("Thoma", "thomas.greveon@gmail.com", [book3])
Tome_Rater.add_user("Tho", "thomas.@gmail.com", [book1])
Tome_Rater.add_user("Tho", "thomas.@gmail.nimp", [book1])
print(Tome_Rater.books)
Tome_Rater.print_catalog()
Tome_Rater.print_users()
print(Tome_Rater.get_most_read_book())
Tome_Rater.add_book_to_user(bookbook, "thomas.grevedon@gmail.com", 4)
Tome_Rater.add_book_to_user(bookbook, "thomas.greveon@gmail.com", 2)
Tome_Rater.add_book_to_user(bookbookbof, "thomas.grevedon@gmail.com", 2)
Tome_Rater.add_book_to_user(bookbookbof, "thomas.@gmail.com", 2)
Tome_Rater.add_book_to_user(bookbookbof1, "thomas.@gmail.com", 2)
Tome_Rater.add_book_to_user(bookbookbof2, "thomas.@gmail.com", 2)
Tome_Rater.add_book_to_user(bookbookbof3, "thomas.@gmail.com", 2)
Tome_Rater.add_book_to_user(bookbookbof4, "thomas.@gmail.com", 2)
Tome_Rater.add_book_to_user("je fais un autre test", "thomas.@gmail.com", 2)
print(Tome_Rater.highest_rated_book())
print(Tome_Rater.most_positive_user())
for ref in Book.instances:
    book = ref()
    isbn_list = []
    isbn_list.append(book.isbn)
print(3456 in isbn_list)
print(Tome_Rater)
print(Tome_Rater.get_n_most_read_books(4))
print(Tome_Rater.get_n_most_read_books(4))
print(Tome_Rater.get_n_most_read_books(4))
print(Tome_Rater.get_n_most_read_books(4))
print(Tome_Rater.get_n_most_prolific_user(15))
print("-----------------------------------------------------------------------------------")
Tome_Rater.print_users()
print(Tome_Rater.get_n_most_prolific_user(3))
print(Tome_Rater.get_n_most_prolific_user(3))
Tome_Rater.print_users()
print(Tome_Rater.get_n_most_expensive_books(5))
Tome_Rater.get_n_most_expensive_books(5)

print(Tome_Rater.get_worth_of_user("thomas.@gmail.com"))



"""
ideas
Ask the user to decide what he wants to do and get the most efficient books on a certain topic"
Put some introduction sentence before outputs
sorted elements?
add commments of book in string in string

add a message about number of users for the most prolific Users

do the 2 last functions about price of books
try to create a chatboat and see if I add extra stuff like comment (? not so sure) tu prends un bouquin et tu cherche dans chaque user. comments si le bouquin est là est tu affiche le comment
OU autre idee c'est de chercher les utilisateur qui ont donné un certain rating au bouquin et d'afficher les commentaires. dans user creer dico avec livre qui renvoie à une liste de valeur [ratin, comment]
Put some introduction sentence before outputs
add comments and clean
upload
"""
