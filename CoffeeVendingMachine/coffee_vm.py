from typing import List

# from typing_extensions import Self
from enums import CoffeeType, ToppingType
from coffee import Coffee
from coffee_maker import CoffeeMaker
from coffee_decorator import ExtraSugarDecorator, CaramelSyrumDecorator
from cvm_state import CVMState, ReadyState
import threading


class CoffeeVM:
    """
    CONTEXT (State Pattern): Holds the current state object and delegates requests to it.
    SINGLETON PATTERN: Ensures only one instance of the Vending Machine exists globally.
    """

    _instance = None
    _lock = threading.Lock()  # Thread-safe lock for Singleton implementation.

    # OOD: Controls object creation to enforce the Singleton pattern.
    def __new__(cls):
        if cls._instance is None:
            # Double-Checked Locking for thread safety.
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance

    # Encapsulation: Initializes the machine's internal state.
    def __init__(self):
        if not self._initialized:
            self._state: CVMState = ReadyState()
            self._selected_coffee: Coffee = None
            self._money_inserted = 0
            self._initialized = True

    @classmethod
    def get_instance(cls):
        # Public accessor for the Singleton instance.
        return cls()

    def select_coffee(self, coffee_type: CoffeeType, toppings: List[ToppingType]):
        # OOD: Uses Factory to create the base coffee.
        coffee = CoffeeMaker.make_coffee(coffee_type)

        # OOD: Uses Decorator to wrap the base coffee with toppings.
        for topping in toppings:
            if topping == ToppingType.EXTRA_SUGAR:
                coffee = ExtraSugarDecorator(coffee)
            elif topping == ToppingType.CARAMEL_SYRUP:
                coffee = CaramelSyrumDecorator(coffee)

        # State Delegation: Passes the request to the current state object.
        self._state.select_coffee(self, coffee)

    def insert_money(self, amount: int):
        self._state.insert_money(self, amount)

    def dispense_coffee(self):
        self._state.dispense_coffee(self)

    def cancel(self):
        self._state.cancel(self)

    def set_state(self, state: CVMState):
        # State Management: The core mechanism for changing the machine's behavior.
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
        # Encapsulation: Provides a controlled way to reset the transaction state.
        self._selected_coffee = None
        self._money_inserted = 0
