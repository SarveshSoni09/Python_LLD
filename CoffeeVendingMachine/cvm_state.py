from abc import ABC, abstractmethod
from CoffeeVendingMachine.coffee import Coffee
from CoffeeVendingMachine.coffee_vm import CoffeeVM
from inventory import Inventory
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from coffee_vm import CoffeeVM
    from coffee import Coffee


class CVMState(ABC):
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
    def select_coffee(self, machine: CoffeeVM, coffee: Coffee):
        machine.set_selected_coffee(coffee)
        machine.set_state(SelectingState())
        print(f"{coffee.get_coffee_type()} selected. Price: {coffee.get_price()}")

    def insert_money(self, machine: CoffeeVM, amount: int):
        print("Please select a coffee first.")

    def dispense_coffee(self, machine: CoffeeVM):
        print("Please select and pay first.")

    def cancel(self, machine: CoffeeVM):
        print("Nothing to cancel.")


class SelectingState(CVMState):

    def select_coffee(self, machine: "CoffeeVM", coffee: "Coffee"):
        print("Already selected. Please pay or cancel.")

    def insert_money(self, machine: "CoffeeVM", amount: int):
        machine.set_money_inserted(machine.get_money_inserted() + amount)
        if machine.get_money_inserted() >= machine.get_selected_coffee().get_price():
            machine.set_state(PaidState())

    def dispense_coffee(self, machine: "CoffeeVM"):
        print("Please insert enough money first.")

    def cancel(self, machine: "CoffeeVM"):
        print(f"Transaction cancelled. Refunding {machine.get_money_inserted()}")
        machine.reset()
        machine.set_state(ReadyState())


class PaidState(CVMState):
    def select_coffee(self, machine: "CoffeeVM", coffee: "Coffee"):
        print("Already paid. Please dispense or cancel.")

    def insert_money(self, machine: "CoffeeVM", amount: int):
        machine.set_money_inserted(machine.get_money_inserted() + amount)
        print(f"Additional {amount} inserted. Total: {machine.get_money_inserted()}")

    def dispense_coffee(self, machine: "CoffeeVM"):
        inventory = Inventory.get_instance()
        coffee = machine.get_selected_coffee()

        if not inventory.has_ingredients(coffee.get_recipe()):
            print("Sorry, we are out of ingredients. Refunding your money.")
            print(f"Refunding {machine.get_money_inserted()}")
            machine.reset()
            machine.set_state(OutOfIngredientSate())
            return

        inventory.deduct_ingredients(coffee.get_recipe())
        coffee.prepare

        change = machine.get_money_inserted() - coffee.get_price()
        if change > 0:
            print(f"Here's your change: {change}")

        machine.reset()
        machine.set_state(ReadyState())

    def cancel(self, machine: "CoffeeVM"):
        print(f"Transaction cancelled. Refunding {machine.get_money_inserted()}")
        machine.reset()
        machine.set_state(ReadyState())


class OutOfIngredientSate(CVMState):
    def select_coffee(self, machine: "CoffeeVM", coffee: "Coffee"):
        print("Sorry, we are sold out.")

    def insert_money(self, machine: "CoffeeVM", amount: int):
        print("Sorry, we are sold out. Money refunded.")

    def dispense_coffee(self, machine: "CoffeeVM"):
        print("Sorry, we are sold out.")

    def cancel(self, machine: "CoffeeVM"):
        print(f"Refunding {machine.get_money_inserted()}")
        machine.reset()
        machine.set_state(ReadyState())
