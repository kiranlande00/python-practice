# Library Management System

import sys

cool_dict = {}
class Library:

    def __init__(self,lbook,lname):
        self.list_book = lbook
        self.library_name = lname

    def display_book(self):
        print("The book available in our library are:")
        print("======================================")
        for i in self.list_book:
            print(i)
        print("\n")

    def lend_book(self,reqbook):
        if reqbook[0] not in self.list_book:
            print("Sorry!The book is not available currently in the library")
        else:
            if reqbook[0] in self.list_book:
                print("The book has been issued")
                cool_dict.update({reqbook[0]:reqbook[1]})
                self.list_book.remove(reqbook[0])

            else:
                print("Sorry!!!Your request book is already borrowed by",cool_dict[reqbook[0]])

    def return_book(self,returnbook):
        self.list_book.append(returnbook)
        print("Thanks for returning your borrowed book")

    def add_book(self,addbook):
        self.list_book.append(addbook)
        print("Thanks for donating book for our library")


class Student:
    def request_book_(self):
        print("Enter your name")
        self.name = input()
        print("Enter the name of the book you'd like to borrow")
        self.book = input()
        return self.book, self.name

    def return_book_(self):
        print("Enter the name of the book you'd like to return")
        self.book = input()
        return self.book

    def add_book_(self):
        print("Enter the name of the book you'd like to donate")
        self.book = input()
        return self.book


def main():
    print("\n***************LIBRARY MANAGEMENT SYSTEM***************\n")
    library = Library(["The Last Battle", "The Screwtape letters", "The Great Divorce","Half Girlfriend","One Night At The Call Center"],"Cool Library")
    student = Student()
    done = False
    while done == False:

        print("LIBRARY MENU\n")
        print("==============================")
        print("\t1. Display the book")
        print("\t2. Lend the book")
        print("\t3. Return the book")
        print("\t4. Add the book")
        print("\t5. Exit")
        print("==============================")

        choice = int(input("Enter Choice:\n"))
        if choice == 1:
            library.display_book()
        elif choice == 2:
            library.lend_book(student.request_book_())
        elif choice == 3:
            library.return_book(student.return_book_())
        elif choice == 4:
            library.add_book(student.add_book_())
        elif choice == 5:
            sys.exit()

        # print(cool_dict)

main()




