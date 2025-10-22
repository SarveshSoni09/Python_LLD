from enums import Symbol


class Player:
    """
    SINGLE RESPONSIBILITY PRINCIPLE (SRP):
    The Player class's sole responsibility is to maintain the state (name and symbol)
    of a participant in the game. It handles no game logic, board interactions, or scoring.

    ENCAPSULATION:
    The player's attributes (`name` and `symbol`) are managed internally,
    with controlled external access provided only through getter methods.
    """

    def __init__(self, name: str, symbol: Symbol):
        self.name = name
        self.symbol = symbol  # Composition: Player HAS-A Symbol.

    def get_name(self) -> str:
        return self.name

    def get_symbol(self) -> Symbol:
        return self.symbol
