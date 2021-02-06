from Book import Book
from Dvd import Dvd
from Journal import Journal


class LibraryItemGenerator:
    """
    Program to ask user to specify type of library item that they
    want to generate.
    """

    @staticmethod
    def generate_item():
        """
        Generates a item based on input entered by user.
        :return: a Item
        """
        print("What type of item would you like to add to the "
              "catalogue of the library?");
        print("1.Book")
        print("2.Journal")
        print("3.DVD")

        user_input = int((input("Select type of item from the above options:")))
        call_num = input("Enter call number for your item:")
        title = input("Enter title for your item:")
        num_copies = input("Enter the number of copies for your item:")
        author = input("Enter the author for your item:")

        if user_input == 1:
            book_publisher = input("Enter the publisher of your Book:")
            return Book(call_num, title, num_copies, author, book_publisher)

        if user_input == 2:
            journal_publisher = input("Enter the publisher of your journal:")
            name = input("Enter the name of the journal:")
            issue_num = input("Enter the issue number of the journal:")
            return Journal(call_num, title, num_copies, author, journal_publisher, name, issue_num)

        if user_input == 3:
            release_date = input("Enter the release date of dvd:")
            region_code = input("Enter the region code of dvd")
            return Dvd(call_num, title, num_copies, author, release_date, region_code)

