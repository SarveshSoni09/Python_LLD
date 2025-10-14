from vending_machine import VendingMachine
from money import Money


# The demo class is a client that interacts with the Vending Machine.
# It doesn't need to know the internal state of the machine, thanks to the LLD.
class VendingMachineDemo:
    @staticmethod
    def main():
        vending_machine = VendingMachine.get_instance()

        vending_machine.add_product("A1", "Coke", 1.25, 10)
        vending_machine.add_product("A2", "Diet Coke", 1.50, 10)
        vending_machine.add_product("A3", "Sprite", 1.25, 10)
        vending_machine.add_product("B1", "Water", 0.75, 20)
        vending_machine.add_product("B2", "Sparkling Water", 1, 10)
        vending_machine.add_product("C1", "Energy Drink", 3.25, 30)

        print("\n------ Select a Product ------")
        vending_machine.select_product("A1")

        print("\n------ Insert Money ------")
        vending_machine.insert_money(Money.DOL1)
        vending_machine.insert_money(Money.DIME)
        vending_machine.insert_money(Money.DIME)
        vending_machine.insert_money(Money.DIME)

        print("\n------ Dispense Product ------")
        vending_machine.dispense()

        print("\n------ Select another Product ------")
        vending_machine.select_product("C1")

        print("\n------ Insert Money ------")
        vending_machine.insert_money(Money.DOL5)
        vending_machine.insert_money(Money.DOL1)
        vending_machine.insert_money(Money.QUARTER)
        vending_machine.insert_money(Money.NICKEL)

        print("\n------ Dispense Product ------")
        vending_machine.dispense()

        print("\n------ Edge Cases Output ------")
        vending_machine.insert_money(Money.DOL5)
        vending_machine.dispense()
        vending_machine.select_product("B1")
        vending_machine.dispense()
        vending_machine.select_product("B1")
        vending_machine.insert_money(Money.QUARTER)
        vending_machine.dispense()
        vending_machine.insert_money(Money.DOL1)
        vending_machine.dispense()


if __name__ == "__main__":
    VendingMachineDemo.main()
