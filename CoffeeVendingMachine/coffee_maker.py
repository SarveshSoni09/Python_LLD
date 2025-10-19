from enums import CoffeeType
from coffee import Coffee, Cappuccino, Espresso, Latte


class CoffeeMaker:
    """
    SIMPLE FACTORY: Responsible for instantiating the correct concrete Coffee object.
    It isolates the client (CoffeeVM) from the complex instantiation logic.
    """

    @staticmethod
    def make_coffee(coffee_type: CoffeeType) -> Coffee:
        # OCP (Open/Closed Principle) Violation Note: This method must be modified
        # every time a new coffee type is introduced. A better factory (like Factory Method)
        # could avoid this, but Simple Factory is fine for this scale.
        if coffee_type == CoffeeType.ESPRESSO:
            return Espresso()
        elif coffee_type == CoffeeType.CAPPUCCINO:
            return Cappuccino()
        elif coffee_type == CoffeeType.LATTE:
            return Latte()
        else:
            raise ValueError(f"Unsupported coffee type: {coffee_type}")
