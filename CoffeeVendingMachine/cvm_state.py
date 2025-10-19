from abc import ABC, abstractmethod
from inventory import Inventory
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Forward reference to resolve circular dependency between CVM and its states.
    from coffee_vm import CoffeeVM
    from coffee import Coffee


class CVMState(ABC):
    """
    STATE INTERFACE: Defines the contract (interface) for all possible states (Abstraction).
    This ensures Polymorphism: the CoffeeVM can call the same method on any state object.
    """

    # NOTE: The 'machine' argument is passed to allow states to access the context (CoffeeVM)
    # and trigger state transitions.

    @abstractmethod
    def select_coffee(self, machine: "CoffeeVM", coffee: "Coffee"):
        pass

    @abstractmethod
    def insert_money(self, machine: "CoffeeVM", amount: int):
        pass

    @abstractmethod
    def dispense_coffee(self, machine: "CoffeeVM"):
        pass

    @abstractmethod
    def cancel(self, machine: "CoffeeVM"):
        pass


class ReadyState(CVMState):
    """CONCRETE STATE: Machine is ready for a new order."""

    def select_coffee(self, machine: "CoffeeVM", coffee: "Coffee"):
        # State Transition: Ready -> Selecting
        machine.set_selected_coffee(coffee)
        machine.set_state(SelectingState())
        print(f"{coffee.get_coffee_type()} selected. Price: {coffee.get_price()}")

    def insert_money(self, machine: "CoffeeVM", amount: int):
        print("Please select a coffee first.")

    def dispense_coffee(self, machine: "CoffeeVM"):
        print("Please select and pay first.")

    def cancel(self, machine: "CoffeeVM"):
        print("Nothing to cancel.")


class SelectingState(CVMState):
    """CONCRETE STATE: A coffee has been chosen, awaiting payment."""

    def select_coffee(self, machine: "CoffeeVM", coffee: "Coffee"):
        print("Already selected. Please pay or cancel.")

    def insert_money(self, machine: "CoffeeVM", amount: int):
        machine.set_money_inserted(machine.get_money_inserted() + amount)
        # State Transition Check: If money is sufficient, transition to PaidState.
        if machine.get_money_inserted() >= machine.get_selected_coffee().get_price():
            machine.set_state(PaidState())

    def dispense_coffee(self, machine: "CoffeeVM"):
        print("Please insert enough money first.")

    def cancel(self, machine: "CoffeeVM"):
        # State Transition: Selecting -> Ready
        print(f"Transaction cancelled. Refunding {machine.get_money_inserted()}")
        machine.reset()
        machine.set_state(ReadyState())


class PaidState(CVMState):
    """CONCRETE STATE: Enough money has been inserted. Ready to dispense."""

    def select_coffee(self, machine: "CoffeeVM", coffee: "Coffee"):
        print("Already paid. Please dispense or cancel.")

    def insert_money(self, machine: "CoffeeVM", amount: int):
        machine.set_money_inserted(machine.get_money_inserted() + amount)
        print(f"Additional {amount} inserted. Total: {machine.get_money_inserted()}")

    def dispense_coffee(self, machine: "CoffeeVM"):
        inventory = Inventory.get_instance()
        coffee = machine.get_selected_coffee()

        if not inventory.has_ingredients(coffee.get_recipe()):
            # State Transition: Paid -> OutOfIngredientSate (Failure)
            print("Sorry, we are out of ingredients. Refunding your money.")
            print(f"Refunding {machine.get_money_inserted()}")
            machine.reset()
            machine.set_state(OutOfIngredientSate())
            return

        # Core logic: Deduct ingredients, prepare coffee, and handle change.
        inventory.deduct_ingredients(coffee.get_recipe())
        coffee.prepare()

        change = machine.get_money_inserted() - coffee.get_price()
        if change > 0:
            print(f"Here's your change: {change}")

        # State Transition: Paid -> Ready (Success)
        machine.reset()
        machine.set_state(ReadyState())

    def cancel(self, machine: "CoffeeVM"):
        # State Transition: Paid -> Ready
        print(f"Transaction cancelled. Refunding {machine.get_money_inserted()}")
        machine.reset()
        machine.set_state(ReadyState())


class OutOfIngredientSate(CVMState):
    """CONCRETE STATE: Machine is temporarily shut down due to missing ingredients."""

    # All methods prevent normal transactions (specific error behavior for this state).
    def select_coffee(self, machine: "CoffeeVM", coffee: "Coffee"):
        print("Sorry, we are sold out.")

    def insert_money(self, machine: "CoffeeVM", amount: int):
        print("Sorry, we are sold out. Money refunded.")

    def dispense_coffee(self, machine: "CoffeeVM"):
        print("Sorry, we are sold out.")

    def cancel(self, machine: "CoffeeVM"):
        # Allows an administrative escape/reset from the stuck state.
        print(f"Refunding {machine.get_money_inserted()}")
        machine.reset()
        machine.set_state(ReadyState())
