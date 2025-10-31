"""
Singleton service class that acts as the main entry point for the system.
It manages all users and auctions. It handles creating auctions and
scheduling their end times using a thread pool.
"""

from user import User
from auction import Auction
from typing import Dict, List
from decimal import Decimal
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
import threading
import time


class AuctionService:
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        if AuctionService._instance is not None:
            raise Exception("This class is a singleton!")

        self.users: Dict[str, User] = {}
        self.auctions: Dict[str, Auction] = {}
        # Scheduler to automatically end auctions
        self.scheduler = ThreadPoolExecutor(max_workers=10)
        self._shutdown = False

    @staticmethod
    def get_instance():
        """Provides thread-safe access to the singleton instance."""
        if AuctionService._instance is None:
            with AuctionService._lock:
                if AuctionService._instance is None:
                    AuctionService._instance = AuctionService()
        return AuctionService._instance

    def create_user(self, name: str) -> User:
        user = User(name)
        self.users[user.get_id()] = user
        return user

    def get_user(self, user_id: str) -> User:
        return self.users[user_id]

    def create_auction(
        self, item_name: str, description: str, base_price: Decimal, end_time: datetime
    ) -> Auction:
        """Creates an auction and schedules a task to end it at its end_time."""
        auction = Auction(item_name, description, base_price, end_time)
        self.auctions[auction.get_id()] = auction

        # Schedule the auction to end automatically
        delay = (end_time - datetime.now()).total_seconds()
        if delay > 0:
            self.scheduler.submit(self._scheduled_end_auction, auction.get_id(), delay)

        print(
            f"New auction created for '{item_name}' (ID: {auction.get_id()}), ending at {end_time}."
        )
        return auction

    def _scheduled_end_auction(self, auction_id: str, delay: float):
        """Internal task run by the scheduler to end an auction."""
        time.sleep(delay)
        if not self._shutdown:
            self.end_auction(auction_id)

    def view_active_auctions(self) -> List[Auction]:
        return [auction for auction in self.auctions.values() if auction.is_active()]

    def place_bid(self, auction_id: str, bidder_id: str, amount: Decimal):
        """Facade method to place a bid. Delegates logic to the Auction."""
        auction = self.get_auction(auction_id)
        auction.place_bid(self.users[bidder_id], amount)

    def end_auction(self, auction_id: str):
        """Facade method to end an auction. Delegates logic to the Auction."""
        auction = self.get_auction(auction_id)
        auction.end_auction()

    def get_auction(self, auction_id: str) -> Auction:
        auction = self.auctions.get(auction_id)
        if auction is None:
            raise KeyError(f"Auction with ID {auction_id} not found.")
        return auction

    def shutdown(self):
        """Shuts down the thread pool scheduler."""
        self._shutdown = True
        self.scheduler.shutdown(wait=True)
