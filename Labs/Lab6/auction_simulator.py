"""
Demonstrate observer pattern through auction simulation.
"""
from random import random

"""
Submitted
By: Saksham Bhardwaj, A01185352
    Prerna Prerna, A01195525

"""


class AuctionClass:
    """
       Simulates an auction. Is responsible for driving the auctioneer and
       the bidders.
    """
    def __init__(self, item_name, starting_price_bid, bidders=None):
        """
        Initialize an auction. Requires a list of bidders that are
        attending the auction and can bid.
        """
        self._bidders = bidders
        self._item_name = item_name
        self._starting_price_bid = starting_price_bid
        if self._bidders is None:
            self._bidders = []

    @property
    def item_name(self):
        return self._item_name

    @property
    def starting_price_bid(self):
        return self._starting_price_bid

    def add_bidders(self, bidder):
        """
        Add bidders to auction registry.
        """
        self._bidders.append(bidder)

    def register_bidders(self, auctioneer):
        """
         Adds a bidder to the list of tracked bidders.
        """
        for bidder in self._bidders:
            auctioneer.add(bidder)

    def start(self, auctioneer):
        """
        Start the auction process
        """
        print(f"\nAuctioning {self.item_name} starting at"
              f" {'${:,.2f}'.format(self.starting_price_bid)}")
        self.register_bidders(auctioneer)
        auctioneer.start_bid(self._starting_price_bid)
        auctioneer.announce_winner()
        auctioneer.announce_highest_bids()


class AuctioneerClass:
    """
        This class is responsible for tracking the highest bid
        and notifying the bidders if it changes.
    """
    def __init__(self, bidders=[], highest_current_bid=0,
                 highest_current_bidder=0):
        self._bidders = bidders
        self._highest_current_bid = highest_current_bid
        self._highest_current_bidder = highest_current_bidder

    @property
    def highest_current_bid(self):
        return self._highest_current_bid

    @highest_current_bid.setter
    def highest_current_bid(self, bid):
        self._highest_current_bid = bid
        self.notify_bidders()

    @property
    def bidders(self):
        return self._bidders

    @property
    def highest_current_bidder(self):
        return self._highest_current_bidder

    def start_bid(self, price):
        self._highest_current_bidder = "Starting price"
        self.highest_current_bid = price

    def add(self, callback):
        """
        Attaches an observer method as to the list of observer callbacks.
        """
        self._bidders.append(callback)

    def accept_bid(self, name, price):
        """
         Accepts a new bid and updates the highest bid. This notifies all
        the bidders via their callbacks.
        """
        if price > self.highest_current_bid:
            print(f"{name} bid {'${:,.2f}'.format(price)} in response to "
                  f"{self._highest_current_bidder}'s bid of "
                  f"{'${:,.2f}'.format(self._highest_current_bid)}!")
            self._highest_current_bidder = name
            self.highest_current_bid = price

    def notify_bidders(self):
        """
        Executes all the bidder callbacks. Should only be called if the
        highest bid has changed.
        """
        for bidder in self._bidders:
            bidder(self)

    def announce_winner(self):
        """
        Announce the winner of the auctioned item.
        """
        if self.highest_current_bidder != "Starting price":
            print(f"\nThe winner of this auction is "
                  f"{self.highest_current_bidder} at"
                  f" {'${:,.2f}'.format(self._highest_current_bid)}!\n")
        else:
            print(f"No one made any bids!")

    def announce_highest_bids(self):
        """
        Dictionary comprehension for summarising highest bids made by bidders.
        """
        highest_bids = {bidder.name: bidder.highest_bid for bidder in
                        self.bidders}
        print("Highest Bids per Bidder ")
        for bidder, bid in highest_bids.items():
            print(f"Bidder: {bidder} Highest bid:"
                  f" {'${:,.2f}'.format(bid)}")


class BidderClass:
    """
    Represent bidder as callable object.
    """
    def __init__(self, name, budget, bid_increase_perc, bid_probability=None,
                 highest_bid=0):
        """
        Initialise Bidder object.
        """
        self._name = name
        self._budget = budget
        self._bid_probability = bid_probability
        self._bid_increase_perc = bid_increase_perc
        self._highest_bid = highest_bid
        if self._bid_probability is None:
            self._bid_probability = random()

    @property
    def name(self):
        return self._name

    @property
    def bid_probability(self):
        return self._bid_probability

    @property
    def highest_bid(self):
        return self._highest_bid

    def _check_bidder(self, auctioneer):
        """
        Perform check to see if highest bid was made by oneself.
        """
        return auctioneer.highest_current_bidder is not self._name

    def _check_bid(self, auctioneer):
        """
        Check if bid is within budget higher than current highest bid

        """
        bid = auctioneer.highest_current_bid * self._bid_increase_perc
        return self._budget > bid > auctioneer.highest_current_bid

    def make_bid(self, auctioneer):
        """
        Make offering bid to auctioneer.
        """
        bid = auctioneer.highest_current_bid * self._bid_increase_perc
        self._highest_bid = bid

    def __call__(self, auctioneer):
        """
        Allow bidder to place a new bid with the Auctioneer.
        """
        if self._check_bidder(auctioneer) and self._check_bid(auctioneer):
            self.make_bid(auctioneer)
            auctioneer.accept_bid(self._name, self._highest_bid)


def main():

    while True:
        try:
            item_name = input("Name of item being auctioned: ")
            starting_price = float(input("Starting price of the item: "))
            num_of_bidders = int(input("Number of bidders bidding for the item: "))
        except ValueError as e:
            print(f"Invalid input -- {e}")
        else:
            break

    auction = AuctionClass(item_name, starting_price)

    for i in range(num_of_bidders):
        while True:
            try:
                name = input(f"Enter bidder {i + 1}'s name: ").capitalize()
                budget = float(input("Enter Budget of the bidder: "))
                inc_percent = float(input("Enter the Bid increase factor: "))
                if inc_percent <= 1:
                    raise ValueError("Value must be greater "
                                     "than 1.")
            except ValueError as e:
                print(e)
            else:
                auction.add_bidders(BidderClass(name, budget, inc_percent))
                print(f"Bidder {name} added")
                break

    auctioneer = AuctioneerClass()
    auction.start(auctioneer)

    print()
    for bidder in auctioneer.bidders:
        print(f"{bidder.name}'s bid probability: "
              f"{'{:,.2f}'.format(bidder.bid_probability)}")


if __name__ == "__main__":
    main()
