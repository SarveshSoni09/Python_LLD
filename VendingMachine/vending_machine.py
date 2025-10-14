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

    def insert_money(self, money: Money):
        self.current_state.insert_money(money)

    def add_product():
        pass

    def select_product():
        pass

    def dispense():
        pass

    def dispense_prodct():
        pass

    def refund_balance():
        pass

    def reset():
        pass

    def add_balance():
        pass

    def get_selected_product():
        pass

    def set_selected_product_code():
        pass

    def set_state():
        pass

    def get_inventory():
        pass

    def get_balance():
        pass
