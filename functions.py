import datetime


class Library:
    def __init__(self, list_of_books, library_name):
        self.list_of_books = list_of_books
        self.library_name = library_name
        boarded_books = dict()
        for books in self.list_of_books:
            boarded_books.update({books: None})
        self.boarded_books = boarded_books
        self.donated_books = dict()

    @property
    def display_books(self):
        for books in self.list_of_books:
            print(books)
        return "These are the available books in our library"

    def lend_book(self, name, book):
        if self.boarded_books[book] is None:
            self.boarded_books.get(book)
            self.boarded_books[book] = name
            return "Success fully lend the book"
        if self.boarded_books[book] is name:
            return "Ohh! You had lend this book already and not return till now"
        elif self.boarded_books[book] is not None:
            return f"Sorry!\tThe book {book} is boarded by {self.boarded_books[book]}"
        else:
            return f"Sorry!, {book} book Not there in our Library, Firstly Please check the Available book in Library"

    # @classmethod
    def add_book(self, name, donated_books):
        if len(donated_books) > 0:
            self.donated_books.update({name: donated_books})
            for book in donated_books:
                self.boarded_books.update({book: None})
                self.list_of_books.append(book)
            return f"Thank you for Donating {len(donated_books)} books to us"
        else:
            return f"Sorry you had not Enter the name of the books Please Try Again"

    def return_book(self, name, book):
        if self.boarded_books[book] == name:
            self.boarded_books[book] = None
            return f"The {book} book is successfully return the by the {name}"
        elif self.boarded_books[book] != name:
            return f"Sorry! Your name is not registered for the book name {book}"
        else:
            return f"Sorry!, {book} book Not there in our Library, Firstly Please check the Available book in Library"

    def log_file(self):
        with open("Library data.txt", "a") as library_file:
            library_file.write(
                f"\n\n{datetime.datetime.now()}\nLibrary Name = {self.library_name}\nLibrary available books = {self.list_of_books}\n" f"Library Boarded books Data = {self.boarded_books}\nDonated Books = {self.donated_books}\n\n")


def permit(object):
    try:
        command = int(input("Enter 1 to log files and save all the data, Enter 2 to see all the data, "
                            "Enter 3 to see the books owned info, Enter 4 to Reset the file : \t"))
        if command == 1:
            object.log_file()

        elif command == 2:
            with open("Library data.txt", "r") as read_mode:
                read_mode.read()

        elif command == 3:
            for book, person in object.boarded_books.items():
                if person is None:
                    print(f"{book}  :==:  is belong to anyone till now")
                else:
                    print(f"{book} is belong to {person}")

        elif command == 4:
            with open("Library data.txt", "w") as reset_file:
                reset_file.write(f"{datetime.datetime.now()} :=: The file is now rested\n\n\n\n")

        else:
            print("Sir, its Wrong input Please Try again")
            permit(object)
        print("Work had been done, Sir\n")

    except Exception as input_error:
        print("Please Enter The legal input, Your Input is wrong I guess\n\n")


def commands(library_name, object, user_name):
    try:

        command = int(input("Press 1 to display the Available books in Library\nPress 2 to Lead a book from "
                            "Library\nPress 3 to to return the book\nPress 4 to Donate Books\n::"))
        if command == 1:
            object.display_books
            with open("Library data.txt", "a") as library_file:
                library_file.write(
                    f"{datetime.datetime.now()} :=: {user_name} had seen the available books details\n")

        elif command == 2:
            book = input("Which book you what to lend from the Library :\t")
            print(object.lend_book(name, book))
            with open("Library data.txt", "a") as library_file:
                library_file.write(
                    f"{datetime.datetime.now()} :=: {user_name} had lended or board the book name {book}\n")
            print("Due to the Social Distancing, Your Book will be now laying at the counter table, Please just"
                  " go and Collect\n")

        elif command == 3:
            book = input("Which book you what to return :\t")
            print(object.return_book(name, book))
            with open("Library data.txt", "a") as library_file:
                library_file.write(f"{datetime.datetime.now()} :=: {user_name} had return the book name {book}\n")
            print("Due to the Social Distancing, You can just go to the counter table and just keep you books "
                  "then we will collect it\n")

        elif command == 4:
            books_to_donate = input("Enter the name of the books (With applying comma ',') which you want to "
                                    "donate: \t").split(", ")
            print(object.add_book(name, books_to_donate))
            with open("Library data.txt", "a") as library_file:
                library_file.write(f"{datetime.datetime.now()} :=: {user_name} had donated {books_to_donate} To the "
                                   f"{library_name}\n")
            print("Due to the Social Distancing, You can just go to the counter table and just keep the books "
                  "which you are donating, then we will collect it\nAnd a special Gift for you : Please insure "
                  "it at check point\n")

        print(">>>The system had been successfully Updated\nThank you for Choosing us\n\n")

    except Exception as error:
        print("Please Enter The legal input, Your Input is wrong I guess\n\n")
        # print(error)

