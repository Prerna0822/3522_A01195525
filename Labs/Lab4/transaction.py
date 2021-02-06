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
    def __init__(self, amount, purchase_name, budget_category):
        self._amount = amount
        self._purchase_name = purchase_name
        self._budget_category = budget_category
        self._timestamp = datetime.now()

    def get_amount(self):
        """
           Returns the total amount of transaction.
           :return integer
           """
        return self._amount

    def get_purchase_name(self):
        """
        Returns the source of the purchase made.
        :return: a string
        """
        return self._purchase_name

    def get_budget_category(self):
        """
        Returns the category of budget.
        :return: string
        """
        return self._budget_category

    def __str__(self):
        return f"Time: {self._timestamp}\n" \
               f"Purchase: {self._purchase_name}\n" \
               f"Transaction Amount: {self._amount}\n" \
               f"Budget Category: {self._budget_category}"
