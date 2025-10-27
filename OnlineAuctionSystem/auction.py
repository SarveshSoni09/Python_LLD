from typing import List, Set, Optional, TYPE_CHECKING
from bid import Bid
from auction_state import AuctionState
from datetime import datetime
from decimal import Decimal
import uuid
import threading

if TYPE_CHECKING:
    from user import User
    from auction_observer import AuctionObserver


class Auction:
    pass
