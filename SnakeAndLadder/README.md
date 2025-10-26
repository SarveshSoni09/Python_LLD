# Snake and Ladder Game: Low-Level Design (LLD)

## 1. Project Overview

This document outlines the Low-Level Design (LLD) for a classic **Snake and Ladder Game**. The system is built to be flexible and robust, cleanly separating the game's setup, rules, and core logic.

The design's foundation is the **Builder Pattern**, which allows for a clean and readable construction of the `Game` object, ensuring all required components (like the board, players, and dice) are properly configured before the game begins.

---

## 2. System Requirements

The design addresses the following core functional requirements:

1.  **Board Setup:** The system must support a customizable board of any size (e.g., 1-100).
2.  **Board Entities:** The game must allow for the placement of **Snakes** (move down) and **Ladders** (move up).
3.  **Player Management:** The system must support two or more players, tracking each player's position.
4.  **Game Rules:**
    - Players take turns in a round-robin fashion.
    - A player's turn consists of rolling a die and moving their piece.
    - Landing on a snake's head or a ladder's bottom automatically moves the player to the entity's end position.
    - Rolling a 6 grants the player an extra turn.
5.  **Win Condition:** The first player to land _exactly_ on the final square wins. Over-rolling (e.g., rolling a 5 from 97 on a 100-square board) results in a skipped turn.

---

## 3. Project Structure

The project is organized into modular files based on responsibility:

```
/
|-- board_entity.py # Defines the abstract BoardEntity class and concrete Snake/Ladder.
|-- board.py # Defines the Board class, which manages entities and positions.
|-- dice.py # Defines the Dice class for rolling.
|-- player.py # Defines the Player data class.
|-- game_status.py # Defines the GameStatus enumeration.
|-- game.py # The main Game class, which includes the Builder and game loop.
|-- game_demo.py # The executable script (entry point) to run the game.
```

---

## 4. Core Design Patterns

This design leverages several key patterns for a clean and maintainable codebase.

1.  **Builder Pattern**

    - **Implementation:** The nested `Game.Builder` class.
    - **Rationale:** A `Game` object is complex to create; it has multiple required components (board, players, dice). The Builder Pattern provides a fluent, step-by-step interface for constructing this complex object. It also provides a single "gate" (`build()` method) to validate that all required parts are present before the `Game` object is created, ensuring it's always in a valid state.

2.  **Abstraction & Inheritance**

    - **Implementation:** The `BoardEntity` abstract class, with `Snake` and `Ladder` as concrete child classes.
    - **Rationale:** This pattern allows the `Board` to treat snakes and ladders polymorphically. The `Board` doesn't care _if_ an entity is a `Snake` or a `Ladder`; it just knows it's a `BoardEntity` with a start and an end. This also centralizes domain-specific validation (e.g., a snake's head must be > its tail) within the entity classes themselves.

3.  **Single Responsibility Principle (SRP) / Encapsulation**
    - **Implementation:** Each class has one, clear purpose.
    - **Rationale:** The `Dice` class only rolls. The `Player` class only tracks its name and position. The `Board` class only manages positions and entities. The `Game` class coordinates these components. This separation makes the code easy to test, debug, and modify.

---

## 5. Key Design Decisions

Beyond patterns, several key decisions in data structure and logic define this design:

- **Dictionary for Board Entities:** The `Board` class converts a _list_ of entities into a _dictionary (hash map)_ in its constructor.

  - **Reasoning:** This is a classic **space-time tradeoff**. While a list is easier to pass in, a dictionary provides vastly superior `O(1)` (constant time) lookups. This means checking if a player landed on a snake/ladder is instantaneous, rather than requiring an `O(n)` list iteration on every single move.

- **Deque for Turn Management:** The `Game` class uses a `collections.deque` (double-ended queue) to manage the list of players.

  - **Reasoning:** A deque is the perfect data structure for a round-robin system. It provides `O(1)` efficiency for both `popleft()` (getting the current player) and `append()` (putting them at the back of the line). Using a standard list's `pop(0)` would be an `O(n)` operation, which is very inefficient.

- **Recursive Extra Turns:** The `take_turn` method uses a **recursive call** to itself to handle the "roll a 6" rule.
  - **Reasoning:** This is an elegant and simple way to manage extra turns. The main `play` loop is effectively "paused" while the current player takes all their recursive turns. Once their streak of 6s ends, the recursion unwinds, and control returns to the main loop, which then appends the player to the back of the queue.

---

## 6. Low-Level Components

### Classes

| Component          | Type           | Responsibility                                                                                             |
| :----------------- | :------------- | :--------------------------------------------------------------------------------------------------------- |
| **`Game`**         | Class          | The **central facade** and "engine" of the game. Manages the game loop, player turns, and game state.      |
| **`Game.Builder`** | Nested Class   | Implements the **Builder Pattern**. Provides a fluent API to construct and validate a `Game` object.       |
| **`Board`**        | Class          | Manages the board's size and the positions of all snakes and ladders using an efficient dictionary lookup. |
| **`BoardEntity`**  | Abstract Class | A common interface for any object that can be placed on the board, defining a `start` and `end`.           |
| **`Snake`**        | Concrete Class | A `BoardEntity` that moves a player from a high position (`start`) to a low one (`end`).                   |
| **`Ladder`**       | Concrete Class | A `BoardEntity` that moves a player from a low position (`start`) to a high one (`end`).                   |
| **`Player`**       | Class          | A simple data class that holds a player's `name` and current `position` on the board.                      |
| **`Dice`**         | Class          | A single-responsibility class for generating a random roll within a specified range.                       |
| **`GameDemo`**     | Class          | The application's entry point (`main` method). Responsible for setting up and starting the game.           |

### Enumerations

| Enumeration      | Definition                                                                                               |
| :--------------- | :------------------------------------------------------------------------------------------------------- |
| **`GameStatus`** | Defines the possible states of the game (`NOT_STARTED`, `RUNNING`, `FINISHED`) to control the game loop. |
