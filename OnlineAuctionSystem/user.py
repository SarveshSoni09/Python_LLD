"""
Represents a User in the system.
Implements AuctionObserver to receive notifications (like "you've been outbid")
from auctions they participate in.
"""

import uuid
from auction_observer import AuctionObserver
from auction import Auction


class User(AuctionObserver):
    def __init__(self, name: str):
        self.id = str(uuid.uuid4())
        self.name = name

    def get_id(self) -> str:
        return self.id

    def get_name(self) -> str:
        return self.name

    def on_update(self, auction: Auction, message: str):
        """Called by an Auction (Subject) to notify this User (Observer)."""
        print(f"--- Notification for {self.name} ---")
        print(f"Auction: {auction.get_item_name()}")
        print(f"Message: {message}")
        print("----------------------------------\n")
