# Imports the Enum class to create a set of named constants.
from enum import Enum


# Defines the possible types of votes using an Enum.
# This makes the code more readable and prevents errors from using raw strings or numbers.
class VoteType(Enum):
    # Assign integer values for easy calculation of the net vote score.
    UPVOTE = 1
    DOWNVOTE = -1
