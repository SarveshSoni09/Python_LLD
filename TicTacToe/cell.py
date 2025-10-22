from enums import Symbol


class Cell:
    """
    ENCAPSULATION: Represents a single unit on the board.
    It encapsulates the state (the Symbol) of a cell.
    """

    def __init__(self):
        # Default state is the 'T' (Temporary/Empty) Symbol.
        self.symbol = Symbol.T

    def get_symbol(self) -> Symbol:
        return self.symbol

    def set_symbol(self, symbol: Symbol):
        self.symbol = symbol
