from enum import Enum


class Money(Enum):
    PENNY = 0.01
    NICKEL = 0.05
    DIME = 0.1
    QUARTER = 0.25
    DOL1 = 1
    DOL5 = 5
    DOL10 = 10
    DOL20 = 20
    DOL50 = 50
    DOL100 = 100

    def get_value(self) -> float:
        return self.value
