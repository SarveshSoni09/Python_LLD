"""
Defines a simple Enum for the possible states of an auction.
"""

from enum import Enum


class AuctionState(Enum):
    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    CLOSED = "CLOSED"
