from Assignments.Assignment1.users.user import User


class Rebel(User):
    """
    This class represents a Rebel user. A Rebel user has the lowest threshold for a notification
    message and warning message. They will also get locked out of transactions and their account if they exceed
    too many budgets in category.
    """

    def __init__(self, user_name, age, account_no, bank_name, account_balance, budget_list):
        super().__init__(user_name, age, account_no, bank_name, account_balance, budget_list)
        self._percentage_threshold = 0.50
        self._lockout_threshold = 1.00
        self._approach_notification_message = "Hey! What are you doing, you've gone 50% on your budget! Stop spending mate!"
        self._exceed_notification_message = "You've exceeded your budget."

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
        Warn the Rebel if their budgets are close to the limit.
        Rebels get locked out of their budget categories if they are exceeded.
        Rebels also get locked out of all budgets if two or more become locked.
        :param selected_budget: Budget - the specific budget that was updated
        :param budget_list: list[Budget] - all budgets the FAM is managing
        :return: None
        """
        # check if amount spent is over x% of total allocated value
        if selected_budget.get_amount_spent() > selected_budget.get_total_value() * self._percentage_threshold:
            print(self._approach_notification_message)

        # check if amount spent is over lock threshold
        if selected_budget.get_amount_spent() > selected_budget.get_total_value() * self._lockout_threshold:
            print(self._exceed_notification_message)
            selected_budget.lock_out()

        # lock all budgets if more than one is locked
        locked_budgets = 0
        for budget in budget_list:
            if budget.get_is_locked():
                locked_budgets += 1

        if locked_budgets > 1:
            for budget in budget_list:
                budget.lock_out()

    @property
    def get_user_name(self):
        """
        Gets name of User.
        :return: String
        """
        return super(Rebel, self).get_user_name()