import difflib
from LibraryItemGenerator import LibraryItemGenerator


def __init__(self, items_list):
    """
    Intialize the library with a list of books.
    :param items_list: a sequence of book objects.
    """
    self._items_list = items_list


def get_items_list(self):
    """
        Return Catalogue list of Items.
        :return: list of Items
        """
    return self._items_list


def find_books(self, title):
    """
    Find books with the same and similar title.
    :param self:
    :param title: a string
    :return: a list of titles.
    """
    title_list = []
    for library_book in self._items_list:
        title_list.append(library_book.get_title())
    results = difflib.get_close_matches(title, title_list,
                                        cutoff=0.5)
    return results


def add_book(self):
    """
    Add a brand new book to the library with a unique call number.
    """
    call_number = input("Enter Call Number: ")
    title = input("Enter title: ")
    num_copies = int(input("Enter number of copies "
                           "(positive number): "))
    book_data = (call_number, title, num_copies)
    author = input("Enter Author Name: ")
    new_book = Book(book_data[0], book_data[1], book_data[2], author)

    found_book = self._retrieve_book_by_call_number(
        new_book.call_number)
    if found_book:
        print(f"Could not add book with call number "
              f"{new_book.call_number}. It already exists. ")
    else:
        self._book_list.append(new_book)
        print("book added successfully! book details:")
        print(new_book)


def remove_book(self, call_number):
    """
    Remove an existing book from the library
    :param call_number: a string
    :precondition call_number: a unique identifier
    """
    found_book = self._retrieve_book_by_call_number(call_number)
    if found_book:
        self._book_list.remove(found_book)
        print(f"Successfully removed {found_book.get_title()} with "
              f"call number: {call_number}")
    else:
        print(f"book with call number: {call_number} not found.")
