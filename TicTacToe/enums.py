from enum import Enum


class GameStatus(Enum):
    """
    ENUMERATION: Defines the possible terminal and non-terminal states of the game.
    Using an Enum ensures type safety and prevents arbitrary string values for status.
    """

    IN_PROGRESS = "IN_PROGRESS"
    WINNER_X = "WINNER_X"
    WINNER_O = "WINNER_O"
    DRAW = "DRAW"


class Symbol(Enum):
    """
    ENUMERATION: Defines the three possible states for a cell on the board.
    T is used for the TIE or EMPTY state, differentiating it from the player symbols.
    """

    X = "X"
    O = "O"
    T = "T"  # Represents a blank/empty cell.

    def get_char(self):
        # Abstraction: Provides a simple interface to get the printable character.
        return self.value
