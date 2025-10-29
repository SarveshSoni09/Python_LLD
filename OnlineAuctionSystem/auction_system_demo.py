from auction_service import AuctionService
from user import User
from auction import Auction
from bid import Bid
from typing import List
from decimal import Decimal
from datetime import datetime, timedelta
import time


class AuctionSystemDemo:
    @staticmethod
    def main():
        auction_service = AuctionService.get_instance()
        art3mis = auction_service.create_user("Art3mis")
        parzival = auction_service.create_user("Parzival")
        plaidt = auction_service.create_user("PlaidThunder")

        print("==========================================")
        print("        Online Auction System Demo        ")
        print("==========================================")

        auction_duration_seconds = 10
        end_time = datetime.now() + timedelta(seconds=auction_duration_seconds)
        aot_auction = auction_service.create_auction(
            "Attack On Titan",
            "An original Attack on Titan manga 1 signed copy.",
            Decimal("100.00"),
            end_time,
        )
        print()

        def try_place_bid(auction_id: str, user_id: str, amount: Decimal):
            try:
                auction_service.place_bid(auction_id, user_id, amount)
            except (ValueError, Exception) as e:
                print(
                    f"FAILED: {auction_service.get_user(user_id).get_name()} bid of ${amount:.2f}: {e}"
                )

        try_place_bid(aot_auction.get_id(), art3mis.get_id(), Decimal("120.00"))
        time.sleep(0.5)

        try_place_bid(aot_auction.get_id(), parzival.get_id(), Decimal("150.00"))
        time.sleep(0.5)

        try_place_bid(aot_auction.get_id(), plaidt.get_id(), Decimal("200.00"))
        time.sleep(0.5)

        try_place_bid(aot_auction.get_id(), art3mis.get_id(), Decimal("190.00"))
        time.sleep(0.5)

        try_place_bid(aot_auction.get_id(), parzival.get_id(), Decimal("200.00"))
        time.sleep(0.5)

        try_place_bid(aot_auction.get_id(), art3mis.get_id(), Decimal("220.00"))
        time.sleep(0.5)

        try_place_bid(aot_auction.get_id(), plaidt.get_id(), Decimal("250.00"))
        time.sleep(0.5)

        print("\n--- Waiting for auction to end automatically... ---")
        time.sleep(auction_duration_seconds + 1)

        print("\n--- Post Auction Information ---")
        ended_auction = auction_service.get_auction(aot_auction.get_id())

        if ended_auction.get_winning_bid() is not None:
            print(
                f"Auction Winner: {ended_auction.get_winning_bid().get_bidder().get_name()}"
            )
            print(f"Winning Bid: ${ended_auction.get_winning_bid().get_amount():.2f}")
        else:
            print("The auction ended with no bids.")

        print("\nFull Bid History:")
        for bid in ended_auction.get_bid_history():
            print(bid)

        print("\n--- Attempting to bid on an ended auction ---")
        try:
            auction_service.place_bid(
                aot_auction.get_id(), parzival.get_id(), Decimal("300.00")
            )
        except Exception as e:
            print(f"Caught Expected Error: {e}")

        auction_service.shutdown()


if __name__ == "__main__":
    AuctionSystemDemo.main()
