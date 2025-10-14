from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
from money import Money

if TYPE_CHECKING:
    from .vending_machine import VendingMachine


class VMState(ABC):
    def __init__(self, machine: "VendingMachine"):
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


class IdleState(VMState):
    def insert_money(self, money: Money):
        print("Please select a Product before inserting Money.")

    def select_product(self, code: str):
        if not self.machine.get_inventory().is_available(code):
            print("Product out of Stock :(")
            return

        self.machine.set_state(ItemSelectedState)

    def dispense(self):
        pass

    def refund(self):
        pass


class ItemSelectedState(VMState):
    pass


class HasMoneyState(VMState):
    pass


class DispensingState(VMState):
    pass
