# Coffee Vending Machine: Low-Level Design (LLD)

## 1. Project Overview

This document outlines the Low-Level Design (LLD) for a sophisticated **Coffee Vending Machine**. The system is architected around a powerful combination of design patterns to create a solution that is flexible, maintainable, and robust.

The core of the system uses the **State Pattern** to manage the machine's lifecycle, the **Decorator Pattern** to dynamically add toppings to beverages, a **Factory** to create coffee types, and the **Singleton Pattern** to ensure a single, consistent state for the machine and its inventory.

---

## 2. System Requirements

The design addresses the following core functional requirements:

1.  **Beverage Selection:** Users must be able to choose from a variety of base coffee types (e.g., Espresso, Latte, Cappuccino).
2.  **Dynamic Customization:** Users must be able to add optional toppings (e.g., Extra Sugar, Caramel Syrup) to their selected coffee, with each addition affecting the final price and recipe.
3.  **Inventory Management:** The machine must track the stock of all ingredients (coffee beans, milk, etc.) and prevent the sale of items for which ingredients are unavailable.
4.  **Payment and Dispensing:** The system must accept money, track the current balance, dispense the beverage upon successful payment, and provide change.
5.  **Stateful Operations:** The machine must enforce a strict workflow. For example, a user cannot insert money before selecting a coffee, and cannot dispense a coffee before paying in full.
6.  **Transaction Cancellation:** Users must be able to cancel their transaction at any point before dispensing, receiving a full refund of the money inserted.

---

## 3. Project Structure

The project is organized into modular files based on responsibility:

```
/ |-- enums.py # Defines enumerations: CoffeeType, Ingredient, ToppingType. |-- coffee.py # Defines the abstract Coffee class and concrete types (Espresso, etc.). |-- coffee_decorator.py # Defines the abstract CoffeeDecorator and concrete toppings. |-- coffee_maker.py # Defines a simple Factory for creating coffee objects. |-- inventory.py # Defines the singleton Inventory class to manage ingredients. |-- cvm_state.py # Defines the abstract CVMState and all concrete state classes. |-- coffee_vm.py # The main Singleton context class for the system. |-- main.py # The executable script (CoffeeVMDemo) to demonstrate functionality.
```

---

## 4. Core Design Patterns

This design is a showcase of how multiple patterns can work together to solve a complex problem elegantly.

1.  **State Pattern**

    - **Implementation:** The `CVMState` abstract class and its concrete implementations (`ReadyState`, `SelectingState`, `PaidState`, `OutOfIngredientSate`).
    - **Rationale:** The machine's behavior changes dramatically depending on its current state. This pattern encapsulates state-specific logic into separate classes, eliminating a complex web of `if/else` statements in the main `CoffeeVM` class. The `CoffeeVM` (the context) simply delegates actions to its current state object.

2.  **Decorator Pattern**

    - **Implementation:** The `CoffeeDecorator` abstract class and its concrete implementations (`ExtraSugarDecorator`, `CaramelSyrumDecorator`).
    - **Rationale:** This pattern allows for adding new functionalities (toppings) to a coffee object dynamically and transparently. It provides a flexible alternative to subclassing for every possible combination of toppings (e.g., `LatteWithSugar`, `EspressoWithCaramelAndSugar`), avoiding a class explosion.

3.  **Factory Method Pattern** (Simple Factory)

    - **Implementation:** The `CoffeeMaker.make_coffee()` static method.
    - **Rationale:** This pattern decouples the `CoffeeVM` from the concrete instantiation of coffee types. The machine simply requests a `CoffeeType`, and the factory handles the details of creating the correct object (`Espresso`, `Latte`, etc.).

4.  **Singleton Pattern**
    - **Implementation:** The `CoffeeVM` and `Inventory` classes.
    - **Rationale:** The system should have only one instance of the vending machine and its inventory to ensure a single, consistent state. This pattern provides a global point of access and prevents conflicts that would arise from multiple, independent inventory or machine state objects.

---

## 5. Low-Level Components

The design is composed of the following core classes and enumerations:

### Classes

| Component                           | Type           | Responsibility                                                                                                                                      |
| :---------------------------------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`CoffeeVM`**                      | Class          | The **central context** and **facade** of the system. Holds the current state and delegates all user actions to it. Implemented as a **Singleton**. |
| **`Inventory`**                     | Class          | Manages the stock levels of all `Ingredient` items in a thread-safe manner. Implemented as a **Singleton**.                                         |
| **`Coffee`**                        | Abstract Class | Defines the common interface for all coffee beverages, including methods for getting a price, a recipe, and preparing the drink.                    |
| **`Espresso`, `Latte`, etc.**       | Concrete Class | Implementations of the `Coffee` interface for specific base beverages.                                                                              |
| **`CoffeeDecorator`**               | Abstract Class | The base class for all toppings. It wraps a `Coffee` object, allowing behavior to be chained.                                                       |
| **`ExtraSugarDecorator`, etc.**     | Concrete Class | Concrete decorators that add cost, ingredients, and preparation steps for a specific topping.                                                       |
| **`CVMState`**                      | Abstract Class | Defines the common interface for all state classes (`select_coffee`, `insert_money`, etc.).                                                         |
| **`ReadyState`, `PaidState`, etc.** | Concrete Class | Implementations of `CVMState` that define the machine's behavior in each specific context.                                                          |
| **`CoffeeMaker`**                   | Class          | A simple factory responsible for creating instances of concrete `Coffee` types.                                                                     |
| **`CoffeeVMDemo`**                  | Class          | Contains the application entry point (`main` method) to simulate user interactions with the machine.                                                |

### Enumerations

| Enumeration       | Definition                                                                       |
| :---------------- | :------------------------------------------------------------------------------- |
| **`CoffeeType`**  | Defines the available base beverages (e.g., `ESPRESSO`).                         |
| **`Ingredient`**  | Defines all possible ingredients used in recipes (e.g., `COFFEE_BEANS`, `MILK`). |
| **`ToppingType`** | Defines the available toppings that a user can select (e.g., `EXTRA_SUGAR`).     |
