from inventory import Inventory
from money import Money
from product import Product
from states import VMState, IdleState


class VendingMachine:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(VendingMachine, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self) -> None:
        if not hasattr(self, "_initialized") or not self._initialized:
            self.inventory = Inventory()
            self.current_state = IdleState(self)
            self.balance = 0
            self.selected_product_code = None
            self._initialized = True

    @classmethod
    def get_instance(cls):
        return cls()

    # The following methods are the public API of the VendingMachine.
    # They delegate the actual logic to the current state object.
    # This is an example of Loose Coupling.
    def insert_money(self, money: Money):
        self.current_state.insert_money(money)

    def add_product(self, code: str, name: str, price: float, quantity: int) -> Product:
        # The VendingMachine is loosely coupled from the Inventory and Product classes.
        product = Product(code, name, price)
        self.inventory.add_product(code, product, quantity)
        return product

    def select_product(self, code: str):
        self.current_state.select_product(code)

    def dispense(self) -> None:
        self.current_state.dispense()

    def dispense_product(self) -> None:
        product = self.inventory.get_product(self.selected_product_code)
        if self.balance >= product.get_price():
            self.inventory.reduce_stock(self.selected_product_code)
            self.balance -= product.get_price()
            print(f"Dispensed: {product.get_name()}")
            if self.balance > 0:
                print(f"Returning change: {self.balance}")
        self.reset()
        self.set_state(IdleState(self))

    def refund_balance(self) -> None:
        print(f"Refunding: {self.balance}")
        self.balance = 0

    def reset(self) -> None:
        self.balance = 0
        self.selected_product_code = None

    def add_balance(self, value: float) -> None:
        self.balance += value

    def get_selected_product(self) -> Product:
        return self.inventory.get_product(self.selected_product_code)

    def set_selected_product_code(self, code: str) -> None:
        self.selected_product_code = code

    def set_state(self, state: VMState) -> None:
        self.current_state = state

    def get_inventory(self) -> Inventory:
        return self.inventory

    def get_balance(self) -> float:
        return self.balance
