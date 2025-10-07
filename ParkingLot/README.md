# Parking Lot Management System: Low-Level Design (LLD)

## 1. Project Overview

This project presents the Low-Level Design (LLD) for a **Multi-Level Parking Lot Management System**. The system is designed to efficiently manage diverse vehicle types, track real-time spot availability, and ensure thread-safe operations across multiple entry and exit points.

## 2. System Requirements

The design addresses the following core functional requirements:

1. **Multi-Level Architecture:** The parking facility must support multiple **Levels**, each containing various parking spots.

2. **Vehicle Diversity:** The system must accommodate different **Vehicle** types (e.g., **Car**, **Motorcycle**, and **Truck**).

3. **Spot Allocation:** Each **Parking Spot** must be dedicated to a specific vehicle type to ensure proper placement.

4. **Assignment & Release:** The system must assign an appropriate parking spot upon vehicle entry and release the spot upon exit.

5. **Real-Time Status:** The system must continuously track and provide real-time availability information for customers.

6. **Concurrency:** The system must handle concurrent access from multiple entry and exit points in a thread-safe manner.

## 3. Low-Level Components

The design is built upon the following core classes, interfaces, and enumerations:

### Classes and Interfaces

| Component         | Type           | Responsibility                                                                                                                                                      |
| ----------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`ParkingLot`**  | Class          | The **central manager** of the entire system. Maintains a list of all levels and coordinates the high-level logic for parking and unparking.                        |
| **`Level`**       | Class          | Represents a single floor of the parking lot. Manages the spot inventory for its floor and is responsible for finding the most suitable spot within its boundaries. |
| **`ParkingSpot`** | Class          | Represents an individual parking space. Tracks its current **availability** status and the specific **`Vehicle`** currently occupying it.                           |
| **`Vehicle`**     | Abstract Class | The base class for all vehicle types. Provides common properties (e.g., license plate) and is extended for specific vehicle types.                                  |
| **`Car`**         | Subclass       | Concrete implementation of a vehicle requiring a standard (medium) spot.                                                                                            |
| **`Bike`**        | Subclass       | Concrete implementation of a vehicle requiring a small spot.                                                                                                        |
| **`Truck`**       | Subclass       | Concrete implementation of a vehicle requiring a large spot.                                                                                                        |
| **`Main`**        | Class          | Contains the application entry point to demonstrate the initialization and operational usage of the `ParkingLot` system.                                            |

### Enumerations

| Enumeration       | Definition                                                                                                                                                             |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`VehicleType`** | Defines the accepted categories of vehicles supported by the system (e.g., `CAR`, `MOTORCYCLE`, `TRUCK`). This enum is used to match a vehicle to an appropriate spot. |

## 4. Design Patterns & Concurrency

### Design Pattern Used

The design utilizes the **Singleton Pattern** for the **`ParkingLot`** class.

- **Rationale:** Ensuring that only **one instance** of the `ParkingLot` object exists globally is crucial, as this object manages the sole, shared resource (the parking spot inventory) and maintains system-wide consistency.

### Concurrency Strategy

To meet the requirement for thread-safe operations from multiple gates, **multi-threading is achieved through the use of the `locks` on critical sections** (e.g., methods that modify spot availability counts or assign/release a `ParkingSpot`).

This ensures that:

1. Only one thread can execute a critical section of code at a time.

2. The shared state (parking spot list, availability counts) remains consistent, preventing race conditions during simultaneous entry or exit operations.
