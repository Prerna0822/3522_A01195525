from Item import Item


class Book(Item):
    """
    Represents a single book in a library which is identified through
    it's call number.
    """

    def __init__(self, call_num, title, num_copies, author, publisher):
        """
        :param call_num: a string
        :param title: a string
        :param num_copies: an int
        :param author: a string
        :param publisher: a publisher
        :precondition call_num: a unique identifier
        :precondition num_copies: a positive integer
        """
        super().__init__(call_num, title, num_copies, author)
        self._publisher = publisher

    def __repr__(self):
        return f"{super().__repr__()}\n" \
               f"Publisher:{self._publisher}"\


    def __str__(self):
        return f"{super().__repr__()}\n" \
               f"Publisher:{self._publisher}"\
