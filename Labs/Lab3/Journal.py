from Item import Item


class Journal(Item):
    """
    Represents a single journal in a library which is identified through
    it's call number.
    """

    def __init__(self, call_num, title, num_copies, author, publisher, name, issue_num):
        """
        :param call_num: a string
        :param title: a string
        :param num_copies: an int
        :param author: a string
        :param publisher: a publisher
        :param name: a name
        :param issue_num: a issue number
        :precondition call_num: a unique identifier
        :precondition num_copies: a positive integer
        """
        super().__init__(call_num, title, num_copies, author)
        self._publisher = publisher
        self._name = name
        self._issue_num = issue_num

    def __repr__(self):
        return f"{super().__repr__()}\n" \
               f"Publisher:{self._publisher}\n" \
               f"Journal Name:{self._name}" \
               f"Issue Number:{self._issue_num}" \

    def __str__(self):
        return f"{super().__repr__()}\n" \
               f"Publisher:{self._publisher}\n" \
               f"Journal Name:{self._name}\n"\
               f"Issue Number:{self._issue_num}"