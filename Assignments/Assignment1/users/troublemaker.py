from Assignments.Assignment1.users.user import User


class Troublemaker(User):
    """
    This class represents an Troublemaker user. An Troublemaker user has the second highest threshold for a notification
    message and warning message. They will also get locked out of transactions if they exceed a budget in category too
    much.
    """

    def __init__(self, user_name, age, account_no, bank_name, account_balance, budget_list):
        super().__init__(user_name, age, account_no, bank_name, account_balance, budget_list)
        self._percentage_threshold = 0.75
        self._lockout_threshold = 1.20
        self._approach_notification_message = "You're nearing the limit for this budget."
        self._exceed_notification_message = "You've exceeded a budget category! Maybe cut back on the spending?"

    def get_threshold(self):
        """
        Get the threshold specific to this type of user.
        :return: float
        """
        return self._percentage_threshold

    def get_lockout_threshold(self):
        """
        Get the lockout threshold specific to this type of user.
        :return: float
        """
        return self._lockout_threshold

    def lockout_budgets(self, selected_budget, budget_list):
        """
        Notify and warn the Troublemaker if their budgets are close to the limit.
        Troublemakers get locked out of their budget categories if they are exceeded.
        :param selected_budget: Budget - the specific budget that was updated
        :param budget_list: list[Budget] - all budgets the FAM is managing
        :return: None
        """
        # check if amount spent is over x% of total allocated value
        if selected_budget.get_amount_spent() > selected_budget.get_budget_value() * self._percentage_threshold:
            print(self._approach_notification_message)

        # check if amount spent is over lock threshold
        if selected_budget.get_amount_spent() > selected_budget.get_budget_value() * self._lockout_threshold:
            print(self._exceed_notification_message)
            selected_budget.lock_out()

    @property
    def get_user_name(self):
        """
        Gets name of User.
        :return: String
        """
        return super(Troublemaker, self).get_user_name()