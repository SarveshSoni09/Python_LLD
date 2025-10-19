from coffee_vm import CoffeeVM
from inventory import Inventory
from enums import CoffeeType, ToppingType, Ingredient


class CoffeeVMDemo:
    @staticmethod
    def main():
        # LLD: Access the single instance via the Singleton pattern.
        machine = CoffeeVM.get_instance()
        inventory = Inventory.get_instance()

        # Initial setup: Refill inventory
        print("=== Initializing Vending Machine ===")
        inventory.add_stock(Ingredient.COFFEE_BEANS, 50)
        inventory.add_stock(Ingredient.WATER, 500)
        inventory.add_stock(Ingredient.MILK, 200)
        inventory.add_stock(Ingredient.SUGAR, 100)
        inventory.add_stock(Ingredient.CARAMEL_SYRUP, 50)
        inventory.print_inventory()

        # Scenario 1: Successful Purchase of a Latte
        print("\n--- SCENARIO 1: Buy a Latte (Success) ---")
        # Abstraction: Client specifies type and toppings, unaware of Decorator implementation.
        machine.select_coffee(CoffeeType.LATTE, [])
        machine.insert_money(7)
        machine.insert_money(3)  # Total 10, price is 8
        machine.dispense_coffee()
        inventory.print_inventory()

        # Scenario 2: Purchase with Insufficient Funds & Cancellation
        print("\n--- SCENARIO 2: Buy Espresso (Insufficient Funds & Cancel) ---")
        machine.select_coffee(CoffeeType.ESPRESSO, [])
        machine.insert_money(5)  # Price is 7
        # State Delegation: This call will be handled by SelectingState
        machine.dispense_coffee()  # Should fail
        machine.cancel()  # Should refund 5 (SelectingState logic)
        inventory.print_inventory()  # Should be unchanged

        # Scenario 3: Attempt to Buy with Insufficient Ingredients
        print("\n--- SCENARIO 3: Buy Cappuccino (Out of Milk) ---")
        # Manipulate inventory to force the OutOfIngredientSate transition
        inventory.deduct_ingredients({Ingredient.MILK: 150})
        inventory.print_inventory()
        # Decorator Pattern Example: Order a complex, decorated coffee
        machine.select_coffee(
            CoffeeType.CAPPUCCINO, [ToppingType.CARAMEL_SYRUP, ToppingType.EXTRA_SUGAR]
        )
        machine.insert_money(15)
        # State Delegation: PaidState will detect lack of Milk, transition to OutOfIngredientSate
        machine.dispense_coffee()  # Should fail and refund
        inventory.print_inventory()

        # Refill and final test
        print("\n--- REFILLING AND FINAL TEST ---")
        inventory.add_stock(Ingredient.MILK, 200)  # Simulates restock
        inventory.print_inventory()
        # CVM is in OutOfIngredientSate, cancel() acts as a necessary admin reset.
        machine.cancel()

        machine.select_coffee(CoffeeType.LATTE, [ToppingType.CARAMEL_SYRUP])
        machine.insert_money(20)
        machine.dispense_coffee()
        inventory.print_inventory()


if __name__ == "__main__":
    CoffeeVMDemo.main()
