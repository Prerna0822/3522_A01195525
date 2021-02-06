from Item import Item


class Dvd(Item):
    """
    Represents a single dvd in a library which is identified through
    it's call number.
    """

    def __init__(self, call_num, title, num_copies, author, release_date, region_code):
        """
        :param call_num: a string
        :param title: a string
        :param num_copies: an int
        :param author: a string
        :param release_date: a release date
        :param region_code: a region code
        :precondition call_num: a unique identifier
        :precondition num_copies: a positive integer
        """
        super().__init__(call_num, title, num_copies, author)
        self._release_date = release_date
        self._region_code = region_code

    def __repr__(self):
        return f"{super().__repr__()}\n" \
               f"Release Date:{self._release_date}\n" \
               f"Region Code:{self._region_code}"\


    def __str__(self):
        return f"{super().__repr__()}\n" \
               f"Release Date:{self._release_date}\n" \
               f"Region Code:{self._region_code}\n"