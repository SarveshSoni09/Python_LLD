# This class follows SRP, only representing a product and its attributes.
class Product:
    def __init__(self, code: str, name: str, price: float) -> None:
        self.code = code
        self.name = name
        self.price = price

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price
