# Import necessary classes for type hinting and functionality.
from vote_type import VoteType
from user import User
from datetime import datetime


# Defines a Vote object, which represents a single vote cast by a user.
class Vote:
    def __init__(self, voter: User, vote_type: VoteType):
        """
        Initializes a Vote object.

        Args:
            voter: The User object who cast the vote.
            vote_type: The type of vote (UPVOTE or DOWNVOTE).
        """
        self.voter = voter
        self.vote_type = vote_type
        self.creation_date = datetime.now()
