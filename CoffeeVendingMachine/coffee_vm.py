from typing import List
from typing_extensions import Self
from enums import CoffeeType, ToppingType
from coffee import Coffee
from coffee_maker import CoffeeMaker
from coffee_decorator import ExtraSugarDecorator, CaramelSyrumDecorator
from cvm_state import CVMState, ReadyState
import threading


class CoffeeVM:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self._state = ReadyState()
            self._selected_coffee: Coffee = None
            self._money_inserted = 0
            self._initialized = True

    @classmethod
    def get_instance(cls):
        return cls()

    def select_coffee(self, coffee_type: CoffeeType, toppings: List[ToppingType]):
        coffee = CoffeeMaker.make_coffee(coffee_type)

        for topping in toppings:
            if topping == ToppingType.EXTRA_SUGAR:
                coffee = ExtraSugarDecorator(coffee)
            elif topping == ToppingType.CARAMEL_SYRUP:
                coffee = CaramelSyrumDecorator(coffee)

        self._state.select_coffee(self, coffee)

    def insert_money(self, amount: int):
        self._state.insert_money(self, amount)

    def dispense_coffee(self):
        self._state.dispense_coffee(self)

    def cancel(self):
        self._state.cancel(self)

    def set_state(self, state: CVMState):
        self._state = state

    def get_state(self) -> CVMState:
        return self._state

    def set_selected_coffee(self, coffee: Coffee):
        self._selected_coffee = coffee

    def get_selected_coffee(self) -> Coffee:
        return self._selected_coffee

    def set_money_inserted(self, amount: int):
        self._money_inserted = amount

    def get_money_inserted(self) -> int:
        return self._money_inserted

    def reset(self):
        self._selected_coffee = None
        self._money_inserted = 0
