from user import User
import random

# Prerna Prerna, A01195525
# Saksham Bhardwaj,A01185352
"""
This class has all the menu options which allow the user to view budget, record transaction,view transaction by budget,
and view bank account details.
"""


class Menu:

    def __init__(self, user_list):
        """
        :param user_list:
        """
        self._user_list = user_list

    def start(self):
        print("1 - REGISTER\n"
              "2 - LOGIN\n"
              "3 - EXIT\n")
        choice = input()

        if choice == 1:
            self.register()
        if choice == 2:
            self.login()
        if choice == 3:
            exit()

    @staticmethod
    def main_menu(user):
        """
        Display the main menu
        """
        user_input = None
        while user_input != 5:
            print("1 - VIEW BUDGET")
            print("2 - RECORD TRANSACTION")
            print("3 - VIEW TRANSACTION BY BUDGET")
            print("4 - VIEW BANK ACCOUNT DETAILS")
            print("5 - LOG OUT")
            string_input = input("Please enter your choice (1-5)")

            if string_input == '':
                continue

            user_input = int(string_input)

            if user_input == 1:
                user.get_budget()

            elif user_input == 2:
                user.record_transaction()

            elif user_input == 3:
                user.record_transaction_budget()
            elif user_input == 4:
                user.view_bank_details()
            elif user_input == 5:
                pass
            else:
                print("Invalid number!! Please enter a"
                      " number from 1 - 5.")

    def register(self):
        """
        Allow the user to register the details of the new user.
        :return: bank details
        """
        user_name = input("Please enter a name: ")
        age = input("Please enter an age: ")
        account_no = random.randint(0, 1000)
        bank_name = input("Please enter a bank: ")
        new_user = User(user_name, age, account_no, bank_name, 0)

        self._user_list.append(new_user)
        self.main_menu(new_user)

    def login(self):
        """
        Allows the user to login into system.
        :return:
        """
        user = input("Please enter name: ")
        if user in self._user_list:
            self.main_menu(user)
        else:
            print("Sorry user not found! try again")
            self.login()

    def view_budget(self, user):
        """ Method for viewing budget."""

    def record_transaction(self, user):
        """Method for recording transaction"""

    def view_transaction_budget(self, user):
        """Method for viewing transaction budget."""

    def view_bank_details(self, user):
        """Method for viewing bank details of the user."""
