from users.angel import Angel
from users.rebel import Rebel
from users.troublemaker import Troublemaker
from budget import Budget

"""
Utility functions for use in other classes; generating test user data.
"""


def load_test_angel():
    """
    Create a test Angel user for use in the FAM.
    :return: Angel
    """
    return Angel(
        "Amy",
        500,
        1234567,
        "TD",
        2000.00,
        [
            Budget("Games and Entertainment", 200),
            Budget("Clothing and Accessories", 200),
            Budget("Eating Out", 200),
            Budget("Miscellaneous", 200)
        ]
    )


def load_test_troublemaker():
    """
    Create a test Troublemaker user for use in the FAM.
    :return: Troublemaker
    """
    return Troublemaker(
        "Karen",
        700,
        101892099,
        "Scotia Bank",
        2000.00,
        [
            Budget("Games and Entertainment", 200),
            Budget("Clothing and Accessories", 200),
            Budget("Eating Out", 200),
            Budget("Miscellaneous", 200)
        ]
    )


def load_test_rebel():
    """
    Create a test Rebel user for use in the FAM.
    :return: Rebel
    """
    return Rebel(
        "Jenny",
        900,
        987654321,
        "CIBC",
        2000.00,
        [
            Budget("Games and Entertainment", 200),
            Budget("Clothing and Accessories", 200),
            Budget("Eating Out", 200),
            Budget("Miscellaneous", 200)
        ]
    )


def load_test_users():
    """
    Create a list of test users, one from each user type. For use in FAM initialization.
    :return: list[User]
    """
    return [load_test_angel(), load_test_troublemaker(), load_test_rebel()]