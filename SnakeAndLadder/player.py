class Player:
    """
    SRP: Responsible only for the player's identity and current position.
    It has no knowledge of the board, dice, or game rules.
    """

    def __init__(self, name: str):
        self.name = name
        self.position = 1  # Initial position is hardcoded (usually 1 or 0).

    # Encapsulation: Accessors for the player's state.
    def get_name(self):
        return self.name

    def get_position(self):
        return self.position

    def set_position(self, position: int):
        self.position = position
