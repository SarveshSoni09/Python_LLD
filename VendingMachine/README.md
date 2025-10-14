# Vending Machine: Low-Level Design (LLD)

## 1. Project Overview

This document outlines the Low-Level Design (LLD) for a **Vending Machine** system. The design robustly handles user interactions by modeling the machine's operations as a series of distinct states. This approach, centered around the **State Design Pattern**, ensures that the machine behaves correctly based on its current context (e.g., idle, waiting for money, dispensing).

The system supports stocking products, handling payments, dispensing items, and providing change, all managed through a clean, state-driven architecture.

---

## 2. System Requirements

The design addresses the following core functional requirements:

1.  **Inventory Management:** The machine must be stockable with various **Products**, each with a unique code, name, price, and quantity.
2.  **Product Selection:** A user must be able to select a product using its code.
3.  **Payment Processing:** The system must accept different denominations of **Money**, track the current balance, and determine if sufficient funds have been inserted.
4.  **Dispensing Logic:** The machine must dispense the selected product if it is in stock and fully paid for. It must also calculate and return any **change**.
5.  **Stateful Operations:** The machine's behavior must change based on user actions. For example, inserting money should only be possible after a product has been selected.
6.  **Error Handling:** The system must handle invalid operations gracefully, such as selecting an out-of-stock item or attempting to dispense without sufficient payment.

---

## 3. Project Structure

The project is organized into modular files, each with a specific responsibility:

/
|-- product.py # Defines the Product data class.
|-- inventory.py # Defines the Inventory class to manage products and stock.
|-- money.py # Defines the Money enumeration for currency.
|-- states.py # Defines the abstract VMState and all concrete state classes.
|-- vending_machine.py # The main Singleton controller class for the system.
|-- main.py # The executable script to demonstrate functionality.

---

## 4. State Machine Diagram

The core of the design is a finite state machine that dictates the flow of operations. Each state handles user input differently and is responsible for transitioning the machine to the next appropriate state.

The primary states and transitions are:

- **Idle:** The machine is waiting for a product selection.
- **ProductSelected:** A valid product has been chosen. The machine is now waiting for money.
- **HasMoney:** Sufficient money for the selected product has been inserted. The machine is ready to dispense.
- **Dispensing:** The machine is in the process of dispensing the product and calculating change.

---

## 5. Low-Level Components

The design is composed of the following core classes and enumerations:

### Classes

| Component                  | Type           | Responsibility                                                                                                                                                                                   |
| :------------------------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`VendingMachine`**       | Class          | The **central context** and **facade** of the system. It holds the current state, inventory, and balance, delegating all operations to its current state object. Implemented as a **Singleton**. |
| **`Inventory`**            | Class          | Manages the collection of available `Product` objects and their stock quantities. Provides methods to check availability and reduce stock.                                                       |
| **`Product`**              | Class          | A simple data class representing an item in the vending machine, with properties for its code, name, and price.                                                                                  |
| **`VMState`**              | Abstract Class | Defines the common interface for all state classes (`insert_money`, `select_product`, etc.). Ensures all states can be treated polymorphically.                                                  |
| **`IdleState`**            | Concrete Class | Handles behavior when the machine is waiting for a user to select a product. Rejects money insertion.                                                                                            |
| **`ProductSelectedState`** | Concrete Class | Handles behavior after a product is selected. Accepts money and transitions to `HasMoneyState` once the balance is sufficient.                                                                   |
| **`HasMoneyState`**        | Concrete Class | Handles behavior when enough money has been inserted. Rejects product selection and initiates dispensing upon request.                                                                           |
| **`DispensingState`**      | Concrete Class | Handles behavior while the product is being dispensed. Rejects all other user inputs during this process.                                                                                        |
| **`VendingMachineDemo`**   | Class          | Contains the application entry point (`main` method) to stock the machine and simulate user interactions.                                                                                        |

### Enumerations

| Enumeration | Definition                                                                                                    |
| :---------- | :------------------------------------------------------------------------------------------------------------ |
| **`Money`** | Defines the available currency denominations (from `PENNY` to `DOL100`) and their corresponding float values. |

---

## 6. Design Patterns Used

The design incorporates several key patterns:

1.  **State Pattern:** This is the foundational pattern of the project.

    - **Rationale:** It encapsulates the behavior of the vending machine into separate state objects. The `VendingMachine` (context) object delegates its behavior to the current state object. This eliminates complex `if/else` conditional logic within the `VendingMachine` class, making the system easier to understand, maintain, and extend (e.g., adding a `MaintenanceState`).

2.  **Singleton Pattern:** Applied to the **`VendingMachine`** class.

    - **Rationale:** A vending machine is a singular entity. This pattern ensures that there is only one instance of the machine managing the inventory and state, preventing data inconsistencies that could arise from multiple instances.

3.  **Facade Pattern:** The **`VendingMachine`** class acts as a facade.
    - **Rationale:** It provides a simple, unified interface (`insert_money()`, `select_product()`) to the client. This hides the complex internal workings of the state transitions and inventory management from the end-user or demo script.
