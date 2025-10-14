# The 'typing' module is used for type hinting, which improves code readability and allows static analysis.
from typing import Dict, Optional
from product import Product


# This class follows the Single Responsibility Principle (SRP) by managing only the inventory.
class Inventory:
    # Encapsulation: The internal data structures (product_map and stock_map) are hidden.
    def __init__(self):
        self.product_map: Dict[str, Product] = {}
        self.stock_map: Dict[str, int] = {}

    def add_product(self, code: str, product: Product, quantity: int) -> None:
        self.product_map[code] = product
        self.stock_map[code] = quantity

    def get_product(self, code: str) -> Optional[Product]:
        # Abstraction: The user of this method doesn't need to know how the product is retrieved.
        return self.product_map.get(code)

    def is_available(self, code: str) -> bool:
        return self.stock_map.get(code, 0) > 0

    def reduce_stock(self, code: str) -> None:
        # Encapsulation: This is the only method that can directly modify the stock level.
        if self.is_available(code):
            self.stock_map[code] -= 1
