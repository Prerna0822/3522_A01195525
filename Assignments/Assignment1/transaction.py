from datetime import datetime

# Prerna Prerna, A01195525
# Saksham Bhardwaj,A01185352

"""
This class declared the variables and methods for the transaction class.
"""


class Transaction:
    """
    :param amount-amount of the transaction
    :param purchase_name - Source of the purchase made
    :param budget_category- Type of budget
    """
    def __init__(self, amount, location):
        self._amount = amount
        self._location = location
        self._timestamp = datetime.now()

    def get_amount(self):
        """
           Returns the total amount of transaction.
           :return integer
           """
        return self._amount



    def get_location(self):
        """
        Returns the category of budget.
        :return: string
        """
        return self._location

    def __str__(self):
        return f"Time: {self._timestamp}\n" \
               f"Transaction Amount: {self._amount}\n" \
               f"Budget Category: {self._location}"
