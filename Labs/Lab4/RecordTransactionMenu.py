from transaction import Transaction
from user import User

# Prerna Prerna, A01195525
# Saksham Bhardwaj,A01185352

"""
This class allows the user to enter and save multiple transactions details
"""


class RecordTransactionMenu:

    def __init__(self, transaction_list):
        self._transaction_list = transaction_list

    # Creating a menu for transactions
    def menu(self):

        user_input = None
        while user_input != 3:
            print("1 - CREATE TRANSACTION")
            print("2 - VIEW TRANSACTIONS")
            print("3 - EXIT")

            string_input = input()

            if string_input == "":
                continue

            user_input = int(string_input)

            if user_input == 1:
                self.create_transaction()
            elif user_input == 2:
                self.transaction_details()
            elif user_input == 3:
                exit()

    """
    This will print all the transaction details of the user by retrieving the data from the list.
    """

    def transaction_details(self):
        print("")
        for transaction in self._transaction_list:
            print(transaction)

    """
    This will allow the user to create a new transaction and then the new transaction will be added to the list.
    """

    def create_transaction(self):
        amount = float(input("Please enter amount: "))
        purchase_name = input("Please enter purchase name: ")
        budget_category = input("Please input budget category: ")
        transaction1 = Transaction(amount, purchase_name, budget_category)
        self._transaction_list.append(transaction1)


"""
Drives the program.
"""


def main():
    User.load_test_user()
    transaction_list = []
    transaction = RecordTransactionMenu(transaction_list)
    transaction.menu()


if __name__ == '__main__':
    main()
