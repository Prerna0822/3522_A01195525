from Assignments.Assignment1.users.user import User


class Angel(User):
    """
    This class represents an Angel user. An angel user has the highest threshold for a notification message and
    warning message.
    """

    def __init__(self, user_name, age, account_no, bank_name, account_balance, budget_list):
        super().__init__(user_name, age, account_no, bank_name, account_balance, budget_list)
        self._percentage_threshold = 0.90
        self._approach_notification_message = "You're nearing the limit for this budget category!"
        self._exceed_notification_message = "You've exceeded a budget category! Maybe cut back on the spending?"

    def get_threshold(self):
        """
        Get the threshold specific to this type of user.
        :return: float
        """
        return self._percentage_threshold

    def lockout_budgets(self, selected_budget, budget_list):
        """
        Politely notify and warn the Angel if their budgets are near or over limit.
        Angels never get locked out.
        :param selected_budget: Budget - the specific budget that was updated
        :param budget_list: list[Budget] - all budgets the FAM is managing
        :return: None
        """
        # check if amount spent is over x% of total allocated value
        if selected_budget.get_amount_spent() > selected_budget.get_budget_value() * self._percentage_threshold:
            print(self._approach_notification_message)

        # check if amount spent is over total value
        if selected_budget.get_amount_spent() > selected_budget.get_budget_value():
            print(self._exceed_notification_message)

    @property
    def get_user_name(self):
        """
        Gets name of User.
        :return: String
        """
        return super(Angel, self).get_user_name()
