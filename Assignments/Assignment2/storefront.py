"""
The storefront module is responsible for receiving and maintaining its
inventory, getting items from a factory class if the store doesn't have
enough stock, and generating the daily transaction report.
"""
# Prerna Prerna, A01195525
# Saksham Bhardwaj,A01185352

from enum import Enum
from orders_processor import *
from datetime import datetime


class InventoryEnum(Enum):
    """
    InventoryEnum is for classifying the amounts of items.
    """
    IN_STOCK = -1
    LOW = 10
    VERY_LOW = 3
    OUT_OF_STOCK = 0

    def __str__(self):
        return str(self.name).title().replace('_', ' ')


class Store:
    """
    A Store is responsible for receiving, maintaining, and retrieving
    order items and generating the daily transaction report.
    """

    def __init__(self):
        """
        Store is initialized with empty inventory and order list.
        """

        self.item_dic = {}
        self.orders = []

    def user_menu(self):
        """
        The interactive menu for the user. The user can process web
        orders, check the inventory, or exit the program and print out
        the daily transaction report.
        """
        print("\nWelcome to the Toy Store!")
        user_input = None
        while user_input != 3:
            print("\nSelect from the following:")
            print("1. Process Web Orders")
            print("2. Check the Inventory")
            print("3. Exit and Print the Daily Transaction Report")
            try:
                user_input = int(input("> "))
            except ValueError:
                print('Enter an integer!')
                continue

            if user_input == 1:
                self.process_orders('orders.xls')

            elif user_input == 2:
                pass
                self.check_inventory()

            elif user_input == 3:
                print("Thank You!")
                self.end_report()
            else:
                print("Invalid option.")

    def process_orders(self, file_name: str) -> None:
        """
        Processes the orders in the provided file and takes the items
        out of inventory, if the item is in an order is not in
        inventory, creates 100 of those items and saves them into
        inventory.
        :param file_name: str
        """
        op = OrderProcessor()
        for an_order in op.process_data(file_name):

            product_id = an_order.product_id
            if product_id not in self.item_dic:
                self.item_dic[product_id] = []

            # if the order contains more than current inventory place
            # 100 more in inventory.
            if an_order.is_valid and \
                    len(self.item_dic[product_id]) < an_order.quantity:
                if an_order.item.lower() == 'candy':
                    for i in range(0, 100):
                        self.item_dic[product_id].append(
                            an_order.factory.create_candy(
                                **an_order.item_details))
                elif an_order.item.lower() == 'stuffedanimal':
                    for i in range(0, 100):
                        self.item_dic[product_id].append(
                            an_order.factory.create_stuffed_animal(
                                **an_order.item_details))
                elif an_order.item.lower() == 'toy':
                    for i in range(0, 100):
                        self.item_dic[product_id].append(
                            an_order.factory.create_toy(
                                **an_order.item_details))

            # subtract the order amount from inventory
            self.item_dic[product_id] = self.item_dic[product_id][
                                        :-an_order.quantity]
            self.orders.append(an_order)

    def end_report(self):
        """
        Creates an end report file placing all the orders in a txt file.
        """
        file_name = 'DTR_' + datetime.today().strftime('%d%m%y_%H%M') + '.txt'
        with open(file_name, 'w') as report:
            for an_order in self.orders:
                report.write(f'{str(an_order)}\n')

    def check_inventory(self):
        """
        Prints all of the inventory by product id and amount of stock.
        """
        for k, v in self.item_dic.items():
            if len(v) <= InventoryEnum.OUT_OF_STOCK.value:
                stock_str = str(InventoryEnum.OUT_OF_STOCK)
            elif len(v) <= InventoryEnum.VERY_LOW.value:
                stock_str = str(InventoryEnum.VERY_LOW)
            elif len(v) <= InventoryEnum.LOW.value:
                stock_str = str(InventoryEnum.LOW)
            else:
                stock_str = str(InventoryEnum.IN_STOCK)
            print(f'Product id: {k} is: {stock_str} with {len(v)}')


def main():
    """Creates a store instance and displays the user menu."""
    store = Store()
    store.user_menu()


if __name__ == '__main__':
    main()