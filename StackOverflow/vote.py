from vote_type import VoteType
from user import User


class Vote:
    def __init__(self, voter: User, vote_type: VoteType):
        self.voter = voter
        self.vote_type = vote_type

    def get_voter(self) -> User:
        return self.voter

    def get_vote_type(self) -> VoteType:
        return self.vote_type
