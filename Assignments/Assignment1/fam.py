import random
from users.angel import Angel
import test_user
from users.rebel import Rebel
from users.troublemaker import Troublemaker
from budget import Budget


class FAM:
    def __init__(self):
        self._users_list = test_user.load_test_users()
        self._selected_user = None
        self._budgets_list = []
        self.budget_details()

    def user_select_budget(self):
        """
        Prompt the user to select a budget to interact with, for use in other menus.
        :return: int - the index of the selected budget in the FAM's budgets_list
        """
        while True:  # repeat until given valid input
            selected_number = 1
            print("Select a Budget")
            for budget in self._budgets_list:
                print(f"{selected_number} - {budget.get_budget_category()}")
                selected_number += 1

            selected_choice = input("Type the number of the budget to select: ")
            if selected_choice.isdigit() and int(selected_choice) in range(1, len(self._budgets_list) + 1):
                return int(selected_choice) - 1
            else:
                print("Invalid input! Please enter av valid value.")

    def view_budgets(self):
        """
        Display budgets to the user with their information.
        :return: None
        """
        print("Your Budgets")
        for budget in self._budgets_list:
            print(budget)

    def create_budget(self, budget_category, budget_value):
        """
        Creates budgets based off the parameters and stores them in self._budgets_list.
        :return: None
        """
        budget = Budget(budget_category, budget_value)
        self._budgets_list.append(budget)

    def budget_details(self):
        """
        Is run on the initialization of a FAM object.
        :return: None
        """
        category_list = ["Games and Entertainment", "Clothing and Accessories",
                         "Eating Out", "Miscellaneous"]
        for i in category_list:
            self.create_budget(i, 0.0)

    def record_transaction(self):
        """
        Handle user input for recording multiple transactions and displaying them.
        :return: None
        """
        finished = False
        while not finished:
            selected_choice = input("Type 't' to record a new transaction or anything else to quit: ")
            if selected_choice.lower() == "t":
                budget = self._budgets_list[self.user_select_budget()]

                budget.record_transaction()
                self._selected_user.lockout_budgets(budget, self._budgets_list)

            else:
                finished = True

    def view_transactions_by_budget(self):
        """
        Displays all transactions for a budget specified by user input.
        :return: None
        """
        selected_budget = self._budgets_list[self.user_select_budget()]
        selected_budget.view_transactions()

    def view_bank_account_details(self):
        """
        Displays bank account details for the User as well as all transactions for each of their Budgets.
        :return: none
        """
        print("Bank Account Information")
        print(self._selected_user.get_bank_details())
        for budget in self._budgets_list:
            budget.view_transactions()

    def display_menu(self):
        """
        Handle user input for interacting with the FAM.
        :return: None
        """
        print("Welcome to the Family Appointed Moderator (FAM)!\n"
              "------------------------------------------------\n")
        input_user = 0
        while input_user != 5:
            print("Press the corresponding number to access the corresponding feature!\n"
                  "1. View Budgets\n"
                  "2. Record a Transaction\n"
                  "3. View Transactions by Budget\n"
                  "4. View Bank Account Details\n"
                  "5. Exit the FAM")
            user_choice = input("Enter your choice: ")

            if user_choice == "":
                continue

            if int(user_choice) == 5:
                break

            method_list = [
                self.view_budgets,
                self.record_transaction,
                self.view_transactions_by_budget,
                self.view_bank_account_details
            ]

            method_list[int(user_choice) - 1]()

        print("Thank you for using the FAM!\n")

    def create_user(self):
        """
        Creates a new user. A user can input their name, age, bank name, bank balance and user type and create a
        new user this way.
        :return: None
        """
        print("Creating new User!\n"
              "------------------------------------------------\n")
        name = input("Enter the name of your user: ")
        age = int(input("Enter the age of your user: "))
        bank_name = input("Enter the bank name of your user: ")
        bank_balance = float(input("Enter the bank balance of your user: "))
        user_type = int(input("Enter the type of your user (1 for Angel, 2 for Troublemaker and 3 for Rebel): "))

        class_list = [Angel, Troublemaker, Rebel]

        new_user = class_list[user_type - 1](name, age, random.randint(1, 999999), bank_name,
                                             bank_balance, [Budget("Games and Entertainment", 200),
                                                            Budget("Clothing and Accessories", 200),
                                                            Budget("Eating Out", 200),
                                                            Budget("Miscellaneous", 200)])
        self._users_list.append(new_user)

    def choose_user(self):
        """
        Chooses a user from a list of generated ones and whatever users you newly create.
        :return: None
        """
        user_input = 0
        while user_input != -1:
            print("Press the corresponding number to access the a user!\n")
            user_number = 1
            for user in self._users_list:
                print(str(user_number) + " - " + user.get_user_name + " (" + user.__class__.__name__ + ")")
                user_number += 1

            user_input = int(input("Enter your choice: "))

            if user_input == self._users_list.index(self._users_list[user_input - 1]) + 1:
                self._selected_user = self._users_list[user_input - 1]
                break

        self.display_menu()

    def main_menu(self):
        """
        The main menu, handles new user registration, login and exiting the entire program.
        :return: None
        """
        input_user = 0
        while input_user != 3:
            print("Press the corresponding number to do something!\n"
                  "1. Register new user\n"
                  "2. Login\n"
                  "3. Exit\n")
            user_choice = input("Enter your choice: ")

            if user_choice == "":
                continue

            if int(user_choice) == 3:
                print("loop")
                break

            method_list = [self.create_user, self.choose_user]

            method_list[int(user_choice) - 1]()

        print("Exiting! Thank you for using the FAM, have a nice day!")


def main():
    fam = FAM()
    fam.main_menu()


if __name__ == '__main__':
    main()