"""
Represents a single Bid, storing the bidder, amount, and timestamp.
Includes comparison logic: higher amount wins; if equal, earlier bid wins.
"""

from datetime import datetime
from decimal import Decimal
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from user import User


class Bid:
    def __init__(self, bidder: "User", amount: Decimal):
        self.bidder = bidder
        self.amount = amount
        self.timestamp = datetime.now()

    def get_bidder(self) -> "User":
        return self.bidder

    def get_amount(self) -> Decimal:
        return self.amount

    def get_timestamp(self) -> datetime:
        return self.timestamp

    def __lt__(self, other: "Bid") -> bool:
        """Compares two bids. Higher amount is 'greater'."""
        if self.amount != other.amount:
            return self.amount < other.amount
        # If amounts are equal, the earlier bid (smaller timestamp) is 'greater'.
        return self.timestamp > other.timestamp

    def __eq__(self, other: "Bid") -> bool:
        return self.amount == other.amount and self.timestamp == other.timestamp

    # ... other comparison methods ...

    def __str__(self) -> str:
        return f"Bidder: {self.bidder.get_name()}, Amount: {self.amount:.2f}, Time: {self.timestamp}"
