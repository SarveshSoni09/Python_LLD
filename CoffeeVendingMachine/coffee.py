from abc import ABC, abstractmethod
from typing import Dict
from enums import Ingredient


class Coffee(ABC):
    """
    ABSTRACT COMPONENT: Defines the interface for all coffee objects,
    both base types and decorated ones (Decorator Pattern).
    """

    def __init__(self):
        self.coffee_type = "Unknown Coffee"

    def get_coffee_type(self) -> str:
        return self.coffee_type

    def prepare(self):
        """Concrete template for basic preparation steps (Template Method flavor)."""

        print(f"\nPreparing your {self.get_coffee_type()}...")
        self._grind_beans()

    def _grind_beans(self):
        print("- Grinding fresh coffee beans.")

    def _brew(self):
        print("- Brewing coffee with hot water.")

    def _pour_into_cup(self):
        print("- Pouring into a cup.")

    @abstractmethod
    def add_condiments(self):
        # Template method step to be implemented by subclasses.
        pass

    @abstractmethod
    def get_price(self) -> int:
        pass

    @abstractmethod
    def get_recipe(self) -> Dict[Ingredient, int]:
        pass


class Espresso(Coffee):
    """CONCRETE COMPONENT: The simplest base coffee."""

    def __init__(self):
        super().__init__()
        self.coffee_type = "Espresso"

    def add_condiments(self):
        pass

    def get_price(self) -> int:
        return 7

    def get_recipe(self) -> Dict[Ingredient, int]:
        # Encapsulation: Defines its own unique ingredient requirements.
        return {Ingredient.COFFEE_BEANS: 7, Ingredient.WATER: 30}


class Latte(Coffee):
    """CONCRETE COMPONENT: A milk-based coffee."""

    def __init__(self):
        super().__init__()
        self.coffee_type = "Latte"

    def add_condiments(self):
        print("- Adding steamed milk.")

    def get_price(self) -> int:
        return 8

    def get_recipe(self) -> Dict[Ingredient, int]:
        return {Ingredient.COFFEE_BEANS: 7, Ingredient.WATER: 30, Ingredient.MILK: 150}


class Cappuccino(Coffee):
    """CONCRETE COMPONENT: A foam-based coffee."""

    def __init__(self):
        super().__init__()
        self.coffee_type = "Cappuccino"

    def add_condiments(self):
        print("- Adding steamed milk and foam.")

    def get_price(self) -> int:
        return 10

    def get_recipe(self) -> Dict[Ingredient, int]:
        return {Ingredient.COFFEE_BEANS: 7, Ingredient.WATER: 30, Ingredient.MILK: 100}
