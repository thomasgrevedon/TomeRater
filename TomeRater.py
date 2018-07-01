"""
**************************************************************************************************************************************
Welcome to TomeRater, an application that allows users to read and rate books.
You have the choice between the following:
    1 - Run the file populate.py by importing this application and get basic functions.
    2 - Uncomment lines 588 and 667 and run this main file and see advanced functions in a static mode.
    3 - Uncomment lines 668 and 670 (please, also keep lines on point 2 uncommented as well to have it working well)
        to get an interactive chatboat style mode function

This application has been realised by Thomas Grevedon (thomas.grevedon@gmail.com) after taking the intensive course on Python
on www.codecademy.com
I hereby would like to thanks all moderators of the course for their support along the learning process.

Disclaimer: as a French speaker, I did my best about English and I apology for any English mistake that you may find.
**************************************************************************************************************************************
"""
import weakref

#creation of the class user that will allow to create user object
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
            if self.books[i] != "None": #This line checks if a rating is associated to a book in the dictionnary of Book attached to the user
                total += self.books[i]
            else:
                continue
        if len(self.books.values()) > 0: #this line makes sure that there is at least one rating before operating the division, otherwise it will divide by 0
            average = total / len(self.books.values())
        return average


#creation of the class book that will allow to create book object
class Book(object):
    instances = set() #This set will help to keep track of the instances of created object Books

    def __init__(self, title, isbn, price = 0):
        self.title = title #this will be a string
        self.isbn = isbn #this will be a number
        self.instances.add(weakref.ref(self))
        self.rating = [] #This will gather all ratings for each book in a list
        self.price = price #this will be a number

    #The following method will help to check if a ISBN already exists and therefore block the creation of Book object (in the bellow methods) if it is the case
    #The method will pull book objects in the set "instances" and check if the attribute ISBN is existing
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
            print("invalid Rating. Please enter a rating between 0 and 4 both included")

    def __eq__(self, other_book):
        if other_book.title == self.title:
            return other_book.isbn == self.isbn

    def get_average_rating(self):
        total = 0
        average = 0
        for i in self.rating:
            total += i
        if len(self.rating) > 0: #this line makes sure that there is at least one rating before operating the division, otherwise it will divide by 0
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
    #The following messages are created as variable since they will be used more than once
    MessageIsbnAlreadyExists = "Sorry, this ISBN already exists, please choose another ISBN for this book"
    MessageUserAlreadyExists = "This user already exists. Please, choose add_book_to_user function in order to add book to this reader! Thanks mate"
    #The following dictionnary will help to keep track of name given to the creation of obejct Bbooks in order ease the use of thos objects such as adding a book to user. It is more easy than remembering the obejct id.
    #this dictionnary will be important for the chatboat mode when asking which book should be added to the user. The user of the application can therefore choose among a list
    bookCreationDictionnary = {}

    def __init__(self):
        self.users = {} #this will map a user's email to the cooresponding User obeject
        self.books = {} #this will map a Book object to the number of Users that have read it

    def create_book(self, title, isbn, price = 0):
        if Book.isIsbnExist(self, isbn) == False: #this line will use the method in the book object to check if the ISBN already exists and will block the method in the class Book returns True
            return Book(title, isbn, price)
        else:
            print(TomeRater.MessageIsbnAlreadyExists) #this messages is printed in case the method t check if an ISBN exist in the class Book returns True

    def create_novel(self, title, author, isbn, price = 0):
        if Book.isIsbnExist(self, isbn) == False: #this line will use the method in the book object to check if the ISBN already exists and will block the method in the class Book returns True
            return Book(title, isbn, price)
            return Fiction(title, author, isbn, price)
        else:
            print(TomeRater.MessageIsbnAlreadyExists) #this messages is printed in case the method t check if an ISBN exist in the class Book returns True

    def create_non_fiction(self, title, subject, level, isbn, price = 0):
        if Book.isIsbnExist(self, isbn) == False: #this line will use the method in the book object to check if the ISBN already exists and will block the method in the class Book returns True
            return Book(title, isbn, price)
            return Non_Fiction(title, subject, level, isbn, price)
        else:
            print(TomeRater.MessageIsbnAlreadyExists) #this messages is printed in case the method t check if an ISBN exist in the class Book returns True

    #the following method will add book (after checking the book has been well created) to a valid user and adds rating in case it is provided
    def add_book_to_user(self, book, email, rating = "None"):
        try:
            self.users[email] #this line checks if the user exists by checking all Keys in the dictionnary self.users
            try:
                book.isbn #this line will check if the book has the attribute ISBN to be sure it has first been created
                self.users[email].read_book(book, rating) #this line will get the user object in self.users and use the read_book method from the user object so it can add the book to the user
                if rating != "None":
                    book.add_rating(rating) #if there is a rating, this line will use the add_rating method in the Book object so it can add a rating to the designated book
                try:
                    self.books[book]
                    self.books[book] += 1 #if the book already exists in the dictionnary self.books, it will add one more reader
                except KeyError:
                    self.books[book] = 1  #if the book does not exist in the dictionnary self.books, it will add it with a value 1 for the first reader
            except AttributeError:
                print("sorry the following book \"{book}\" could not be added to the user as it needs to be created first.".format(book = book))
        except KeyError:
            print("No user with email {email}".format(email = email))

    #This methods is here to create user. It will first check that the user does not already exist and if not it will check the validity of the emal address
    #If books are provided while created the user, it will use the previous above method: add book to user
    def add_user(self, name, email, user_books = "None"):
        try:
            self.users[email] #this line checks if the user exists by checking all Keys in the dictionnary self.users and will block the creation of the user obejct if it the case
            print(TomeRater.MessageUserAlreadyExists)
        except KeyError:
            checkList = ["@", ".edu", '.org', '.com'] # The creation of a user's email address will need to be checked with the checklist. The idea of crating a list is to allow modification on it. '
            sensor = 1 #sensor will iterate on the list checkList from the position 1
            needMessage = True
            while sensor < len(checkList):
                if checkList[0] in email and checkList[sensor] in email: #it needs to get the @ so checkList[0] and one of the extension getting with the sensor that iterates through the cheklist
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
                #The following will occur if the email address of a user is not correct as it might have the "@" and one of the extension analyzed by the sensor in checkList
                #Therefore, the following is a message created for the user with what he needs to use to have a correct email address
                extension = ""
                for i in checkList[1:]:
                    extension += "\"" + i + "\" " #this will get the allowed extension in checklist
                print("Please check the email address of user and make sure it has the following characheters: \"@\" and one of the following extension: " + extension)

    #the following method print the catalog of the object so it gets the titles of self.books printed. Therefore, only the books that have been at least read one time can be printed.
    def print_catalog(self):
        for i in self.books.keys():
            print(i.title)

    def print_users(self):
        for i in self.users.values():
            print(i)

    #The following method will iterates to the values of self.books dictionnary and return the title of the key that goes with the highest value
    def get_most_read_book(self):
        total = 0
        most_read_book = ""
        for i in self.books:
            if self.books[i] > total:
                most_read_book = i.title
                total = self.books[i]
        return most_read_book

    #The following method will iterates in the keys of self.books dictionnary, operates the method to get the average of rating for each book object and return the title of the key that goes with the highest value
    def highest_rated_book(self):
        highest_average = 0
        highest_rated_book = ""
        for i in self.books:
            average_rating = i.get_average_rating()
            if average_rating > highest_average:
                highest_average = average_rating
                highest_rated_book = i.title
        return highest_rated_book

    #The following method will iterates to the values of self.users dictionnary, operates the method to get the average of the User object and return the user object of the key that goes with the highest value
    def most_positive_user(self):
        highest_average = 0
        highest_positive_user = ""
        for i in self.users.values():
            average_rating = i.get_average_rating()
            if average_rating > highest_average:
                highest_average = average_rating
                highest_positive_user = i
        return highest_positive_user

    #The following method takes a number n and iterates trough a copy of the dictionnay self.books to get values of how many times the book has been read
    #Once the value has been gotten, it will be removed from the copy of the dictionnary, added to a list and the process will start again until "n" is reached
    def get_n_most_read_books(self, n = 0):
        total = 0
        new_dict = dict(self.books) #this will create a copy of the dictionnay self.books in order to avoid working on the original one
        ordered_lst = [] #this list will be populated with the value gotten from the copy of the dictionnary
        sensor = 1
        if n <= len(new_dict) and n >= sensor: #this helps to make sure that the number requested does not exceed the number of value in the dictionay and helps to run the process until n is reached by the sensor
            while sensor <= n:
                for i in new_dict:
                    if new_dict[i] > total: #new_dict[i] gets the number of how many time the book has been read.
                        value = i.title #it will get the title of the book
                        valueToRemove = i
                        total = self.books[i] #the value of how many times it has been read gotten on the dictionnary becomes the new total
                ordered_lst.append(value)
                new_dict.pop(valueToRemove)
                total = 0
                sensor += 1
            return ordered_lst
        else:
            return "Please choose a number between 1 and {number} both included".format(number = len(new_dict))

    #the following gets a number n and creates a copy of the dictionn self.users. It will check the numbers of books a user has on the User object by checking the length of user.books
    #Once it has gotten the highest value, it adds the user to a list and removes it from the copied dictionnary and the process will continue until the copied dictionnary is empty
    #At the end it returns n values from the list created with ths users
    def get_n_most_prolific_user(self, n = 0):
        total = 0
        temp_dic = dict(self.users) #creation of a copy of the dictionnary to avoid working on the original one
        mostProlificUsers = []
        if n <= len(temp_dic) and len(temp_dic) > 0: #it checks if the number request with n does not exceed the number of value in self.users dictionnary and makes sure that the dictionnary has at least one entry
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

        #the following method gets a number n and iterates into the set of instances of the class Book. it add the title of each book as a key in a dictionnary and the price as a Value
        #Once the dictionnary is done, it will iterates on it and get the highest value. When it has it, it will add the title to one list and the price to antoher list and remove the entry from the dictionnary
        #it will do that until the dictionnary is empty and then zip both list of title and price. Then it will get values from that zip list and return n sentences with the title of the book and its price
    def get_n_most_expensive_books(self, n=4):
        total = -1
        temp_dic = {} #this will be the created dictionnary from the gotten keys book's title and value book's price
        price_lst = [] #this will be the list of prices gottten from the values of the created dictionnary
        book_name = [] #this will be the list of book names gotten from the keys of the created dictionnary
        #creation of the dictionnary
        if len(Book.instances) > 0:
            for book in Book.instances:
                book = book()
                temp_dic[book.title] = book.price #cration of the dictionnary with the title of the book as key and the price as value
            #wreattion if list of prices and list of names until the created dictionnary is empty
            while len(temp_dic) != 0:
                for book in temp_dic:
                    if temp_dic[book] > total: #this checks if the price of the book is above the total and note that the total is initially equal to -1 as a book can have the value 0 for the price
                        title_to_add = book
                        valueToRemove= book #this the entry that we need to remove from the created dictionnary
                        price_to_add = temp_dic[book]
                        total = temp_dic[book]
                book_name.append(title_to_add) #creation of the list of book name
                price_lst.append(price_to_add) #creation of the list of book price
                temp_dic.pop(valueToRemove)
                total = -1
            nameAndPriceLst = list(zip(book_name, price_lst)) #zip of lists of book name and list of book price
            if n <= len(nameAndPriceLst):
                for tuple in range(0, n):
                    sensor = 0 #the sensor allows us to control the allocation of item gotten in tuple. If sensor = 0 then the item is the title of the book, otherwise it is the price.
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

    #The following method takes a user_email and first check if the user exists. If yes, then it will get each book of this user and find the price of this book in the instances of the class Book
    #then it will sum up  all the prices and return the total of the prices
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
        return "The most read book is \'{book_most_red}\' and the highest rated book is \'{book_highest_rated}\'. The most positive reader is \'{user}\'"\
        .format(book_most_red = self.get_most_read_book(), book_highest_rated = self.highest_rated_book(), user = self.most_positive_user())

    #from this point, the following methods concern only the menu for the chatboat mode
    def MainMenu(self):
        print("Welcome to Tomerater. What would you like to do? Please select one of the following \
         \n [1] Print catalog \n [2] Print users \n [3] Create a book \n [4] Add user \n [5] Add book to user \n [6] Get most read book \
          \n [7] Get highest rated book \n [8] Get most positive user \n [9] Get n most read book \n [10] Get n most prolific users\
          \n [11] Get n most expensive books \n [12] Get worth of user \n [13] Print TomeRater \n [14] Exit")
        n = input()
        print(n)
        if n == "1":
            print("Please find below the catalog but note that only books that have been already read one time are there")
            self.print_catalog()
            print("")
            self.MainMenu()
        elif n == "2":
            self.print_users()
            print("")
            self.MainMenu()
        elif n == "3":
            self.MenuCreateBook()
        elif n == "4":
            self.MenuAddUser()
        elif n == "5":
            self.MenuAddBookToUser()
        elif n == "6":
            print(self.get_most_read_book())
            print("")
            self.MainMenu()
        elif n == "7":
            print(self.highest_rated_book())
            print("")
            self.MainMenu()
        elif n == "8":
            print(self.most_positive_user())
            print("")
            self.MainMenu()
        elif n == "9":
            self.MenuGetMostObjects(9)
        elif n == "10":
            self.MenuGetMostObjects(10)
        elif n == "11":
            self.MenuGetMostObjects(11)
        elif n == "12":
            self.MenuGetWorthOfUser()
        elif n == "13":
            print(self)
            print("")
            self.MainMenu()
        elif n == "14":
            print("End")
        else:
            print("Sorry, you selection is not valid, choose between the number given in the options")
            print("")
            self.MainMenu()


    def MenuCreateBook(self):
        print("Please, write the title of the book")
        title = str(input())
        print("Please give the ISBN of the book")
        isbn = input()
        sensor = 0
        while sensor == 0:
            try:
             int(isbn) #this try is to make sure an integer has been entered by the user. Indeed, we need to pass an integer for the ISBN in order to create a book
             sensor = 1
            except ValueError:
                print("Sorry your input is not valid. Pease insert a number")
                print("Please give the ISBN of the book")
                isbn = input()
        print("Please give the price of the book")
        price = input()
        sensor = 0
        while sensor == 0:
            try:
             int(price) #this try is to make sure an integer has been entered by the user. Indeed, we need to pass an integer for the price in order to create a book
             sensor = 1
            except ValueError:
                print("Sorry your input is not valid. Pease insert a number")
                print("Please give the price of the book")
                price = input()
        print('what reference name would you like to use for the book? Please answer without space')
        name = input().replace(" ", "") #this will be the name added as a key in the dictionnary bookCreationDictionnary in order to help the user to remember which book has been created and to play with it
        booktocreate = self.create_book(title, int(isbn), int(price))
        try:
            booktocreate.isbn #this line is making sure that the object is not going to be added in the dictionnary bookCreationDictionnary if it has not been well created. In order to check if it has been well created, the attribute ISBN is tested on the book
            self.bookCreationDictionnary[name] = booktocreate #Therefore this map the name choosen by the user to help remembering a book wwith a Book object
            self.MainMenu()
        except AttributeError:
            print("Sorry the book could not have been created")
            self.MainMenu()

    def MenuAddUser(self):
        print("What is the name of the user?")
        name = input()
        print("Please give the email addres of the user")
        email = input()
        print("Would you like to add book to this user? \n [1] Yes \n [2] No")
        n = input()
        #here, if the user of the application wants to add books, we are going to ask the user to choose a book to add. So first of all, a list of book that can be added is created by iterating on the Keys of the the dictionnary bookCreationDictionnary
        #Then, a sensor is here to make sure that the user has well selected a book without string. When this is done, the sensor is updated.
        booklst = []
        bookToAdd = []
        if n == "1":
            sensor = 0
            while sensor == 0:
                for book in self.bookCreationDictionnary.keys():
                    booklst.append(book) #creation of the list of book (keys of the dictionnary bookCreationDictionnary)
                print("Please choose one of the following book to add to the user (without strings)")
                print(booklst)
                book = input()
                if book in booklst:
                    bookToAdd.append(self.bookCreationDictionnary[book])
                    sensor = 1 #sensor will be updated once the entry of the user is correct by checking that the entry is on the list of book previously created.
                else:
                    print("Sorry your selection is not valid. Please choose a book among the list")
                    booklst = []
        #Afterwards, the length of bookToAdd is checked in order to see if it has to be mentionned in the arguments
        if len(bookToAdd) > 0:
            self.add_user(name, email, bookToAdd)
        else:
            self.add_user(name, email)
        self.MainMenu()

    #here, like the method above, we are going to first create a list from which the user of the application can choose a book to add to user
    #once the book is choosen and well choosen (checked by sensor), a user needs to be selectd with his email address. A list of email address is created by iterating in keys of the dictionnary self.users
    #Once the email address is choosen and valid (checked by sensor), a valid rating (also checked by sensor) needs to be added if the user of application has decided to add one
    def MenuAddBookToUser(self):
        #selection of the book
        sensor = 0
        booklst = []
        while sensor == 0:
            for book in self.bookCreationDictionnary.keys():
                booklst.append(book) #creation of the list of book
            print("Please choose amoong the list, the book you would like to add (without string)")
            print(booklst)
            book = input()
            if book in booklst:
                bookToAdd = self.bookCreationDictionnary[book]
                sensor = 1 #sensis updated as the entry is valid
            else:
                print("sorry your entry is not correct. Please choose a book among the list")
                booklst = []
        #selection of the user
        sensor = 0
        userlst = []
        while sensor == 0:
            for user in self.users.keys():
                userlst.append(user) #creation of the list user
            print("Please choose among the following email address the one you would like to choose (without string)")
            print(userlst)
            user = input()
            if user in userlst:
                userToSelect = user
                sensor = 1 #sensor is updated if the user is valid
            else:
                print("Sorry your entry is not valid. please check the email address in the list")
                userlst = []
        #From here start the part to add a rating or not.
        print("do you want to add a rating? \n [1] Yes \n [2] No")
        n = input()
        sensor = 0
        if n == "1":
            print("Please give the rating of the book between 0 and 4 both included")
            rating = input()
            while sensor == 0:
                try:
                    int(rating) #this is to esure that an integer as been entered as we will need to pass an integer for the rating
                    ratingToAdd = int(rating)
                    if ratingToAdd < 0 or ratingToAdd > 4:
                        print("Sorry insert a number between 0 and 4 both included")
                        rating = input()
                    else:
                        sensor = 1 #Sensor is updated if the rating is valid.
                except ValueError:
                    print("Sorry your input is not valid. Pease insert a number")
                    print("Please give the rating of the book")
                    rating = input()
        else:
            ratingToAdd = "None" #this is in case the user select 2 and does not want to add a rating
        self.add_book_to_user(bookToAdd, userToSelect, ratingToAdd)
        self.MainMenu()

    #here we can perform three methods under one as they all work in the same way
    #the value X is passed from the Mainmenu and inform which method needs to be used
    #As each method is taking a n number, the user is invited to first say the number
    def MenuGetMostObjects(self, x):
        #First, we ask the user to choose the number from the list of the method that will be performed that he would like to see displayed.
        print("How many books would you like to have on your list? Please insert a number")
        n = input()
        sensor = 0
        while sensor == 0:
            try:
                int(n) #this is to check that the user entered a valid number, otherwise a new entry will be asked and the validy of the entry is checked by a sensor
                if x == 9:
                    print(self.get_n_most_read_books(int(n)))
                elif x == 10:
                    print(self.get_n_most_prolific_user(int(n)))
                else:
                    print(self.get_n_most_expensive_books(int(n)))
                sensor = 1
            except ValueError:
                print("sorry your entry is not valid. Please insert a number")
                n = input()
        self.MainMenu()

    #here we will check the worth value of user. First of all a list of user's email is created by iterating in the keys of the dictionnary self.users.
    #Then the user of the application is required to choose one email address to get the worth value of the user.
    def MenuGetWorthOfUser(self):
        userlst = []
        for user in self.users.keys():
            userlst.append(user) #creation of the list
        print("Please choose among the following email address the one you would like to know the value (without string)")
        print(userlst)
        user = input()
        print(self.get_worth_of_user(user))
        self.MainMenu()


"""
Tome_Rater = TomeRater()
#cerate some books:
Tome_Rater.bookCreationDictionnary["book1"] = Tome_Rater.create_book("Society of Mind", 12345678, 20)
Tome_Rater.bookCreationDictionnary["novel1"] = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345, 15)
Tome_Rater.bookCreationDictionnary["notification1"] = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452, 23)
Tome_Rater.bookCreationDictionnary["notification2"] = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938, 44)
Tome_Rater.bookCreationDictionnary["novel2"] = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010, 12)
Tome_Rater.bookCreationDictionnary["novel3"] = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000, 7)

#create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")

#add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[Tome_Rater.bookCreationDictionnary["book1"], Tome_Rater.bookCreationDictionnary["novel1"], Tome_Rater.bookCreationDictionnary["notification1"]])

#add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(Tome_Rater.bookCreationDictionnary["book1"], "alan@turing.com", 1)
Tome_Rater.add_book_to_user(Tome_Rater.bookCreationDictionnary["novel1"], "alan@turing.com", 3)
Tome_Rater.add_book_to_user(Tome_Rater.bookCreationDictionnary["notification1"], "alan@turing.com", 3)
Tome_Rater.add_book_to_user(Tome_Rater.bookCreationDictionnary["notification2"], "alan@turing.com", 4)
Tome_Rater.add_book_to_user(Tome_Rater.bookCreationDictionnary["novel3"], "alan@turing.com", 1)
Tome_Rater.add_book_to_user(Tome_Rater.bookCreationDictionnary["novel2"], "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(Tome_Rater.bookCreationDictionnary["novel3"], "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(Tome_Rater.bookCreationDictionnary["novel3"], "david@computation.org", 4)

#Using advanced methos on created books and users
print("--> Here is the catalog of TomeRater:")
Tome_Rater.print_catalog()
print("")

print("--> Here is the list of users:")
Tome_Rater.print_users()
print("")

print("--> Here is what happens when we want to create a book with an existing ISBN. The try is to create a book2 called \" Sneaky ISBN \" with the existing ISBN: 12345678")
book2 = Tome_Rater.create_book("Sneaky ISBN", 12345678, 28)
print("")

print("--> Here is what happens when we try to create a user with an invalid email address. The try is to create a user with the email address: user@doesnotwork.fail:")
Tome_Rater.add_user("User", "user@doesnotwork.fail")
print("")

print("--> Here is what happens when we want to add a user that alrady exists:")
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
print("")

print("--> Here is the most read book:")
print(Tome_Rater.get_most_read_book())
print("")

print("--> Here is the highest_rated_book:")
print(Tome_Rater.highest_rated_book())
print("")

print("--> Here is the most positive user:")
print(Tome_Rater.most_positive_user())
print("")

print("--> Here are the 3 most read books:")
print(Tome_Rater.get_n_most_read_books(3))
print("")

print("--> Here are the 2 most prolific users:")
print(Tome_Rater.get_n_most_prolific_user(2))
print("")

print("--> Here are the 4 most expensive books:")
print(Tome_Rater.get_n_most_expensive_books(4))
print("")

print("--> Here is the worth value of the user: Alan Turing with email address: alan@turing.com:")
print(Tome_Rater.get_worth_of_user("alan@turing.com"))
print("")

print("--> Here how TomeRater looks like when it is printed:")
print(Tome_Rater)
print("")
"""
"""
Tome_Rater.MainMenu()
"""
