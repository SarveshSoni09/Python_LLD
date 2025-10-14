from typing import Dict, Optional
from product import Product


class Inventory:
    def __init__(self):
        self.product_map: Dict[str, Product] = {}
        self.stock_map: Dict[str, int] = {}

    def add_product(self, code: str, product: Product, quantity: int) -> None:
        self.product_map[code] = product
        self.stock_map[code] = quantity

    def get_product(self, code: str) -> Optional[Product]:
        return self.product_map.get(code)

    def is_available(self, code: str) -> bool:
        return self.stock_map.get(code, 0) > 0

    def reduce_stock(self, code: str) -> None:
        self.stock_map[code] = self.stock_map[code] - 1
