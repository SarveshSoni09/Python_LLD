# Online Auction System: Low-Level Design (LLD)

## 1. Project Overview

This document outlines the Low-Level Design (LLD) for a **Real-Time Online Auction System**. This is a concurrent system designed to manage multiple auctions, handle simultaneous user bids, and automatically conclude auctions at a scheduled time.

The architecture is a sophisticated combination of the **Singleton** and **Facade** patterns (for the central service), the **Observer** pattern (for real-time notifications), and a **thread pool** for asynchronous event scheduling and execution. The design places a strong emphasis on **thread-safety** and data integrity in a multi-user environment.

---

## 2. System Requirements

The design addresses the following core functional requirements:

1.  **User Management:** The system must be able to create and manage user accounts.
2.  **Auction Creation:** Users must be able to create new auctions for items, specifying a base price and a precise **end time**.
3.  **Bidding System:**
    - Registered users must be able to place bids on active auctions.
    - A new bid must be higher than the current highest bid (or the base price).
4.  **Automatic Expiry:** Auctions must end automatically and precisely at their scheduled `end_time`.
5.  **Notifications (Real-Time):**
    - When a user is outbid, they must be notified immediately.
    - When an auction ends, all participating bidders must be notified of the outcome (winner or no bids).
6.  **Concurrency:** The system must safely handle multiple users bidding on the same item at the same time, as well as handle bids that arrive at the _exact_ moment an auction is scheduled to end.
7.  **Data Integrity:** The system must correctly identify a single, unambiguous winner, even with simultaneous bids.

---

## 3. Project Structure

The project is organized into modular files based on responsibility:

```
/
|-- user.py # Defines the User class, which acts as an Observer.
|-- bid.py # Defines the Bid data class, with comparison logic.
|-- auction_state.py # Defines the AuctionState enumeration (ACTIVE, CLOSED, etc.).
|-- auction_observer.py # Defines the AuctionObserver abstract interface.
|-- auction.py # Defines the Auction class, the "Subject" being observed.
|-- auction_service.py # The main Singleton/Facade class. Manages all services and scheduling.
|-- auction_system_demo.py # The executable script (entry point) to run the demo.
```

---

## 4. Core Design Patterns

This design effectively combines several patterns to manage complex, asynchronous behavior.

1.  **Observer Pattern**

    - **Implementation:** `Auction` is the **Subject** (the observable object), and `User` is the **Observer** (via the `AuctionObserver` interface).
    - **Rationale:** This pattern perfectly decouples the auction from the bidders. When a `User` places a bid, they are automatically subscribed as an observer. When a key event happens (like a new highest bid or the auction's end), the `Auction` object iterates through its list of observers and notifies them, without needing to know _how_ they will react. This is ideal for real-time notifications.

2.  **Singleton Pattern**

    - **Implementation:** The `AuctionService` class.
    - **Rationale:** The system requires a single, centralized authority to manage all users, all auctions, and, most critically, the **`ThreadPoolExecutor`** for scheduling. Having one global scheduler ensures all timed events are managed in one place, preventing resource conflicts and ensuring a single source of truth.

3.  **Facade Pattern**
    - **Implementation:** The `AuctionService` class also acts as a Facade.
    - **Rationale:** It provides a simple, high-level API (`create_auction`, `place_bid`) to the client (`AuctionSystemDemo`). This hides the complex internal orchestration, such as creating an `Auction` object, submitting a scheduled task to the thread pool, and retrieving the correct `User` object to place a bid.

---

## 5. Concurrency & Event Scheduling

This design's most critical feature is its handling of concurrency and time-based events.

- **Asynchronous Event Scheduling (`ThreadPoolExecutor`)**

  - The `AuctionService` maintains a `ThreadPoolExecutor`. When an auction is created, the service submits a new task (`_scheduled_end_auction`) to the pool.
  - This task _sleeps_ for the required duration in a separate thread, leaving the main application thread free. When it wakes, it calls the `end_auction` method. This is a highly scalable and non-blocking approach to managing thousands of auction timers.

- **Thread-Safety (`threading.RLock`)**
  - The `Auction` class uses an `RLock` to protect its critical sections: `place_bid` and `end_auction`.
  - **Rationale:** This lock is essential to prevent **race conditions**. Without it, two users could bid simultaneously, leading to corrupted data (e.g., two "highest" bids). More importantly, it prevents a user from placing a bid at the _exact millisecond_ the scheduled `end_auction` task is running, ensuring a clean and unambiguous end to the auction.

---

## 6. Low-Level Components

### Classes

| Component               | Type           | Responsibility                                                                                                                                                                    |
| :---------------------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`AuctionService`**    | Class          | **Singleton/Facade**. The central entry point. Manages all users, auctions, and the event scheduler (`ThreadPoolExecutor`).                                                       |
| **`Auction`**           | Class          | The **Subject**. Represents a single auction item. Manages its own `state` (e.g., `ACTIVE`), a list of `bids`, and its list of `observers`. All critical methods are thread-safe. |
| **`User`**              | Class          | Represents a participant. Implements the **Observer** interface (`on_update`) to receive notifications from auctions.                                                             |
| **`Bid`**               | Class          | A data class holding the `bidder`, `amount`, and `timestamp`. Implements comparison methods (`__lt__`, `__gt__`, etc.) which are crucial for `max()` to find the highest bid.     |
| **`AuctionObserver`**   | Abstract Class | The **Observer interface**, defining the `on_update` method that all observers must implement.                                                                                    |
| **`AuctionSystemDemo`** | Class          | The application's entry point (`main` method). Simulates user creation, auction setup, and bidding.                                                                               |

### Enumerations

| Enumeration        | Definition                                                                                                                                      |
| :----------------- | :---------------------------------------------------------------------------------------------------------------------------------------------- |
| **`AuctionState`** | Defines the lifecycle of an auction (`PENDING`, `ACTIVE`, `CLOSED`). This is used to enforce rules, like preventing bids on a `CLOSED` auction. |
