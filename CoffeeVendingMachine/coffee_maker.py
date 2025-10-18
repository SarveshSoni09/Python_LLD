from enums import CoffeeType
from coffee import Coffee, Cappuccino, Espresso, Latte


class CoffeeMaker:
    @staticmethod
    def make_coffee(coffee_type: CoffeeType) -> Coffee:
        if coffee_type == CoffeeType.ESPRESSO:
            return Espresso()
        elif coffee_type == CoffeeType.CAPPUCCINO:
            return Cappuccino()
        elif coffee_type == CoffeeType.LATTE:
            return Latte()
        else:
            raise ValueError(f"Unsupported coffee type: {coffee_type}")
