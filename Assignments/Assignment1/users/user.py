import abc


class User(abc.ABC):
    """
    Abstract base class that represents all the necessary information that a user must have to function in the
    FAM system.
    """

    def __init__(self, user_name, age, account_no, bank_name, account_balance, budget_list):
        self._user_name = user_name
        self._age = age
        self._account_no = account_no
        self._bank_name = bank_name
        self._account_balance = account_balance
        self._budget_list = budget_list

    def get_threshold(self):
        """
        Get the threshold specific to this type of user.
        :return: float
        """
        pass

    def get_notification_message(self):
        """
        Get the notification specific to this type of user.
        :return: string
        """
        pass

    def get_bank_details(self):
        """
        Get the bank account details of the user (account number, bank name, bank balance).
        :return: string
        """
        return f"Bank name: {self._bank_name}" \
               f"\nAccount Number: {self._account_no}" \
               f"\nBank balance: {self._account_balance}"

    def lockout_budgets(self, selected_budget, budget_list):
        """
        Lock one or more budgets if needed based on their values and User type.
        :param selected_budget: Budget - the specific budget that was updated
        :param budget_list: list[Budget] - all budgets the FAM is managing
        :return: None
        """
        pass

    def get_user_name(self):
        """
        Gets the name of the User.
        :return: String
        """
        return self._user_name