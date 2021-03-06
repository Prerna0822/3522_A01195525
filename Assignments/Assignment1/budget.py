
from transaction import Transaction


class Budget:
    """
    Class representing a budget for a given category of spending; keeps track of purchases and dollar limits.
    """

    def __init__(self, budget_category: str, budget_value: float):
        self._budget_category = budget_category
        self._budget_value = budget_value
        self._amount_spent = 0.00
        self._transaction_list = []
        self._is_locked = False

    def add_amount_spent(self, amount: float):
        """
        Add an amount of money to the total amount spent this month in the Budget.
        :param amount: float
        :return: None
        """
        self._amount_spent += amount

    def get_budget_value(self):
        """
        Gets the total value of the Budget.
        :return: float
        """
        return self._budget_value

    def get_budget_category(self):
        """
        Gets the category of the Budget.
        :return: String
        """
        return self._budget_category

    def get_is_locked(self):
        """
        Gets the locked state of the Budget.
        :return: Boolean
        """
        return self._is_locked

    def get_amount_spent(self):
        """
        Gets the amount spent in the Budget.
        :return: float
        """
        return self._amount_spent

    def get_amount_remaining(self):
        """
        Calculate the amount of money remaining in the Budget, as the difference between total and spent.
        :return: float
        """
        return self._budget_value - self._amount_spent

    def lock_out(self):
        """
        Locks out a user's budgets completely.
        :return: None
        """
        if not self._is_locked:
            self._is_locked = True

    def add_transaction(self, trans: Transaction):
        """
        Add a new transaction to the list of transactions for this Budget.
        :param trans: Transaction
        :return: None
        """
        self._transaction_list.append(trans)

    def record_transaction(self):
        """
        Create a new Transaction with values from user input; store it in the list for this Budget.
        :return: None
        """
        if self.get_is_locked():
            print(f"{self._budget_category} budget is locked! Cannot record transaction.")
            return

        print(f"Recording Transaction in {self._budget_category}")
        location = input("Enter the store or website you shopped at: ")
        amount = float(input("Enter the amount spent: "))

        trans = Transaction(amount, location)
        self.add_transaction(trans)
        self.add_amount_spent(amount)

        print("Transaction recorded!\n")

    def view_transactions(self):
        """
        Print a list of all Transactions made in this Budget.
        :return: None
        """
        print(f"Transactions in category {self._budget_category} this month")
        if not self._transaction_list:
            print("No transactions made so far.")
        else:
            for transaction in self._transaction_list:
                print(transaction)

    def __str__(self):
        """
        Represent the object as a formatted string.
        :return: str
        """

        is_locked_string = "is" if self._is_locked else "is not"

        # :.2f formats to 2 decimal places inside f-string
        return f"~~[ Budget for {self._budget_category} ] ~~" \
               f"\n- Total allocated: ${self._budget_value:.2f}" \
               f"\n- Amount spent so far this month: ${self._amount_spent:.2f}" \
               f"\n- Amount remaining for this month: ${self.get_amount_remaining():.2f}" \
               f"\n- This budget {is_locked_string} locked\n"


def main():
    temp = Budget("Shopping", 200.00)
    print(temp)
    temp.record_transaction()
    temp.view_transactions()
    print(temp)


if __name__ == '__main__':
    main()