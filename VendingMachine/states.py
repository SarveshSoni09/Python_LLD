from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
from money import Money

# Forward reference to avoid circular imports.
if TYPE_CHECKING:
    from .vending_machine import VendingMachine


# The VMState abstract class defines the contract for all states of the vending machine.
# This is a core part of the State design pattern.
class VMState(ABC):
    def __init__(self, machine: "VendingMachine"):
        # The state holds a reference to the context (the VendingMachine).
        self.machine = machine

    @abstractmethod
    def insert_money(self, money: Money):
        pass

    @abstractmethod
    def select_product(self, code: str):
        pass

    @abstractmethod
    def dispense(self):
        pass

    @abstractmethod
    def refund(self):
        pass


# IdleState represents the initial state. Its behavior is encapsulated here.
# It follows the Open/Closed Principle (OCP) - if we need a new state, we create a new class.
class IdleState(VMState):
    def __init__(self, machine: "VendingMachine"):
        super().__init__(machine)

    def insert_money(self, money: Money):
        # Behavior specific to the Idle state.
        print("Please select a Product before inserting Money.")

    def select_product(self, code: str):
        if not self.machine.get_inventory().is_available(code):
            print("Product out of Stock :(")
            return

        self.machine.set_selected_product_code(code)
        # Polymorphism in action: The machine's behavior changes by setting a new state object.
        self.machine.set_state(ProductSelectedState(self.machine))
        print(f"Product Selected: {code}")

    def dispense(self):
        print("No Product Selected.")

    def refund(self):
        print("No Money to Refund")


class ProductSelectedState(VMState):
    def __init__(self, machine: "VendingMachine"):
        super().__init__(machine)

    def insert_money(self, money: Money):
        self.machine.add_balance(money.get_value())
        print(
            f"Money inserted: {money.get_value()}! Balance: {self.machine.get_balance()}"
        )

        selected_product = self.machine.get_selected_product()
        # This state is responsible for checking if the balance is sufficient.
        if (
            selected_product
            and self.machine.get_balance() >= selected_product.get_price()
        ):
            print("Sufficient money received.")
            self.machine.set_state(HasMoneyState(self.machine))

    def select_product(self, code: str):
        print(
            "Product already selected. Please insert money or request refund to select another product."
        )

    def dispense(self):
        print("Please insert sufficient money.")

    def refund(self):
        self.machine.refund_balance()
        self.machine.reset()
        self.machine.set_state(IdleState(self.machine))


class HasMoneyState(VMState):
    def __init__(self, machine: "VendingMachine"):
        super().__init__(machine)

    def insert_money(self, money: Money):
        self.machine.add_balance(money.get_value())
        print(f"More Money inserted: {money.get_value()} - will be returned as change.")

    def select_product(self, code: str):
        print(
            "Product already selected. Please insert money or request refund to select another product."
        )

    def dispense(self):
        self.machine.set_state(DispensingState(self.machine))
        self.machine.dispense_product()

    def refund(self):
        self.machine.refund_balance()
        self.machine.reset()
        self.machine.set_state(IdleState(self.machine))


class DispensingState(VMState):
    def __init__(self, machine: "VendingMachine"):
        super().__init__(machine)

    def insert_money(self, money: Money):
        print("Currently dispensing, please wait.")

    def select_product(self, code: str):
        print("Currently dispensing, please wait.")

    def dispense(self):
        print("Dispensing in progress...")

    def refund(self):
        print("Dispensing in progress, refund not allowed.")
