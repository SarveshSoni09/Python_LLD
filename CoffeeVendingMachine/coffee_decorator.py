from coffee import Coffee
from typing import Dict
from enums import Ingredient


class CoffeeDecorator(Coffee):
    """
    ABSTRACT DECORATOR: Base class for all coffee enhancements.
    Inherits from Coffee (Component Interface) to ensure type compatibility (LSP).
    Holds a reference to the wrapped object (Composition).
    """

    def __init__(self, coffee: Coffee):
        # Composition: The decorator contains the object it is decorating.
        super().__init__()
        self.decorated_coffee = coffee

    # Delegation: All core operations are delegated to the wrapped object.
    def get_price(self) -> int:
        return self.decorated_coffee.get_price()

    def get_recipe(self) -> Dict[Ingredient, int]:
        return self.decorated_coffee.get_recipe()

    def add_condiments(self):
        return self.decorated_coffee.add_condiments()

    def prepare(self):
        return self.decorated_coffee.prepare()


class ExtraSugarDecorator(CoffeeDecorator):
    """
    CONCRETE DECORATOR: Adds sugar-related cost and ingredient requirements.
    """

    COST = 1
    RECIPE_ADDITION = {Ingredient.SUGAR: 1}

    def __init__(self, coffee: Coffee):
        super().__init__(coffee)

    def get_coffee_type(self) -> str:
        # Overrides: Enhances the description by recursively calling the wrapped object's method.
        return self.decorated_coffee.get_coffee_type() + ", Extra Sugar"

    def get_price(self) -> int:
        # Overrides: Adds its specific cost to the decorated coffee's total price.
        return self.decorated_coffee.get_price() + self.COST

    def get_recipe(self) -> Dict[Ingredient, int]:
        # Overrides: Merges its required ingredients with the base recipe.
        new_recipe = self.decorated_coffee.get_recipe().copy()
        for ingredient, qty in self.RECIPE_ADDITION.items():
            # Ensures correct merging, handling case where sugar might already be in recipe.
            new_recipe[ingredient] = new_recipe.get(ingredient, 0) + qty
        return new_recipe

    def prepare(self):
        # Extends: Executes the base preparation first, then adds its unique action.
        super().prepare()
        print("- Stirring in Extra Sugar.")


class CaramelSyrumDecorator(CoffeeDecorator):
    """
    CONCRETE DECORATOR: Adds caramel syrup-related cost and ingredient requirements.
    """

    COST = 2
    RECIPE_ADDITION = {Ingredient.CARAMEL_SYRUP: 10}

    def __init__(self, coffee: Coffee):
        super().__init__(coffee)

    def get_coffee_type(self) -> str:
        return self.decorated_coffee.get_coffee_type() + ", Caramel Syrup"

    def get_price(self) -> int:
        return self.decorated_coffee.get_price() + self.COST

    def get_recipe(self) -> Dict[Ingredient, int]:
        # Overrides: Merges its required ingredients with the base recipe.
        new_recipe = self.decorated_coffee.get_recipe().copy()
        for ingredient, qty in self.RECIPE_ADDITION.items():
            new_recipe[ingredient] = new_recipe.get(ingredient, 0) + qty
        return new_recipe

    def prepare(self):
        super().prepare()
        print("- Drizzling Caramel Syrup on top.")
