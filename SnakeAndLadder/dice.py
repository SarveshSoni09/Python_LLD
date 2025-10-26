import random


class Dice:
    """
    SRP: Sole responsibility is to simulate a die roll.
    Loose Coupling: The Game class only depends on the 'roll()' method, allowing
    easy swapping for different dice types (e.g., loaded dice, multiple dice).
    """

    def __init__(self, min_val: int, max_val: int):
        self.min_val = min_val
        self.max_val = max_val

    def roll(self) -> int:
        return random.randint(self.min_val, self.max_val)
