class User:

    # Prerna Prerna, A01195525
    # Saksham Bhardwaj,A01185352
    """
    This class has all the details related to a user.
    """

    def __init__(self, user_name, age, account_no, bank_name, account_balance):
        """
        user account details
        :param user_name:
        :param age:
        :param account_no:
        :param bank_name:
        :param account_balance:

        """
        self._user_name = user_name
        self._age = age
        self._account_no = account_no
        self._bank_name = bank_name
        self._account_balance = account_balance

    def get_user_name(self):
        """
        Returns the name of the user.
        :return: a string
        """
        return self._user_name

    def get_age(self):
        """
        Returns the age of the user.
        :return: integer
        """
        return self._age

    def get_account_no(self):
        """
        Returns the account number of the user.
        :return: a number
        """
        return self._account_no

    def get_account_balance(self):
        """
        Return the account balance of the user.
        :return: a number
        """
        return self._account_balance

    def set_account_balance(self, value):
        """
        Assigning a value to the account_balance variable
        :param value: account_balance
        :return: a number
        """
        self._account_balance = value

    def __str__(self):
        return f"Name of the user: {self.get_user_name()}" \
               f"Age of the user: {self.get_age()}" \
               f"Account Number: {self.get_account_no()}" \
               f"Bank Name: {self._bank_name}" \
               f"Account Balance: {self._account_balance}" \
 \


    @staticmethod
    def load_test_user():

        test_user = User("Amy", 19, 10103872, "Scotia Bank", 5999)
        return test_user
