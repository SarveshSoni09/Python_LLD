# Tic-Tac-Toe Game: Low-Level Design (LLD)

## 1. Project Overview

This document outlines the Low-Level Design (LLD) for a **Tic-Tac-Toe Game**. This is not a simple implementation; it is a highly extensible and robust system built using a combination of powerful design patterns.

The design's core revolves around the **State Pattern** to manage the game's flow, the **Strategy Pattern** to define win conditions, and the **Observer Pattern** to decouple the game logic from components like a scoreboard. This architecture makes the game easy to maintain, test, and extend with new features.

---

## 2. System Requirements

The design addresses the following core functional requirements:

1.  **Core Gameplay:** The system must support a 3x3 grid for two players (X and O) who take turns placing their marks.
2.  **Win Detection:** The game must automatically detect a win condition (three in a row, column, or diagonal).
3.  **Draw Detection:** The game must detect a draw condition (the board is full, and no winner is found).
4.  **Turn Management:** The system must enforce player turns, preventing a player from moving twice.
5.  **Invalid Moves:** The system must reject invalid moves, such as placing a mark on an already occupied cell or an out-of-bounds position.
6.  **Scoring:** The system must track scores (number of wins) for each player across multiple games.
7.  **Extensibility:** The design should be extensible, allowing for potential future changes like a different board size or new win conditions.

---

## 3. Project Structure

The project is organized into modular files based on responsibility:

```
/
|-- enums.py # Defines enumerations: GameStatus, Symbol.
|-- cell.py # Defines the Cell class, a single square on the board.
|-- board.py # Defines the Board class, which manages the grid of Cells.
|-- player.py # Defines the Player data class.
|-- invalid_move_exception.py # Custom exception for invalid game moves.
|-- win_strategy.py # Defines the WinStrategy interface and concrete win-checking classes.
|-- game_state.py # Defines the GameState interface and concrete states (InProgress, Draw, Winner).
|-- game_observer.py # Defines the GameObserver interface.
|-- game_subject.py # Defines the GameSubject (observable) interface.
|-- scoreboard.py # A concrete observer that tracks player scores.
|-- game.py # The core Game class, which acts as the State context and the Subject.
|-- tic_tac_toe.py # The main Singleton/Facade class for the entire system.
|-- tic_tac_toe_demo.py # The executable script to demonstrate functionality.
```

---

## 4. Core Design Patterns

This design effectively combines several key patterns to create a clean, decoupled architecture.

1.  **State Pattern**

    - **Implementation:** The `GameState` abstract class and its concrete implementations: `InProgressState`, `WinnerState`, and `DrawState`.
    - **Rationale:** This pattern encapsulates the game's behavior based on its current status. The `Game` class holds a reference to a `GameState` object and delegates the `handle_move` action to it. This cleanly separates the logic for what happens during a move, when the game is won, or when it's a draw, eliminating complex `if/else` logic in the main game class.

2.  **Strategy Pattern**

    - **Implementation:** The `WinStrategy` abstract class and its concrete implementations: `RowWinningStrategy`, `ColWinningStrategy`, and `DiagonalWinningStrategy`.
    - **Rationale:** This pattern decouples the win-checking logic from the `Game` class. The `Game` class holds a _list_ of these strategies and simply iterates through them to check for a winner. This is highly extensible; a new win condition (e.g., "four corners") could be added simply by creating a new strategy class, with no changes to the `Game` class itself.

3.  **Observer Pattern**

    - **Implementation:** The `GameSubject` (implemented by `Game`) and `GameObserver` (implemented by `Scoreboard`) interfaces.
    - **Rationale:** This pattern decouples the `Game` from other components that need to react to its events. When a game ends (win or draw), the `Game` object calls `notify_observers()`. The `Scoreboard` object, which is "subscribed" to the game, receives this update and increments the winner's score. Other observers (like a logger or an analytics service) could be added just as easily.

4.  **Singleton Pattern**

    - **Implementation:** The `TicTacToe` class.
    - **Rationale:** This pattern ensures that only one instance of the main game-hosting system exists. This is critical for managing a single, persistent `Scoreboard` that tracks scores across multiple game sessions.

5.  **Facade Pattern**
    - **Implementation:** The `TicTacToe` class also acts as a facade.
    - **Rationale:** It provides a simple, high-level API (`create_game`, `make_move`, `print_board`) to the outside world (the demo script). This hides the complex internal interactions between the `Game`, `GameState`, `Board`, `Players`, and `WinStrategy` objects.

---

## 5. Low-Level Components

The design is composed of the following core classes and enumerations:

### Classes

| Component             | Type           | Responsibility                                                                                                                                                 |
| :-------------------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`TicTacToe`**       | Class          | The **central facade** and **singleton instance** of the system. Manages game creation and the persistent `Scoreboard`.                                        |
| **`Game`**            | Class          | The main game engine. Acts as the **Context** for the State pattern and the **Subject** for the Observer pattern. Holds the board, players, and current state. |
| **`Board`**           | Class          | Represents the 3x3 game board. Manages a 2D array of `Cell` objects and tracks the move count.                                                                 |
| **`Player`**          | Class          | A simple data class holding a player's name and their `Symbol` (X or O).                                                                                       |
| **`Cell`**            | Class          | Represents a single square on the board, holding a `Symbol`.                                                                                                   |
| **`GameState`**       | Abstract Class | The interface for the **State Pattern**. Defines the `handle_move` method.                                                                                     |
| **`InProgressState`** | Concrete Class | State implementation for when the game is actively being played.                                                                                               |
| **`WinnerState`**     | Concrete Class | State implementation for when the game is over and has a winner. Rejects new moves.                                                                            |
| **`DrawState`**       | Concrete Class | State implementation for when the game is a draw. Rejects new moves.                                                                                           |
| **`WinStrategy`**     | Abstract Class | The interface for the **Strategy Pattern**. Defines the `check_winner` method.                                                                                 |
| **`Row/Col/Diag...`** | Concrete Class | Concrete strategy implementations for checking all win conditions.                                                                                             |
| **`GameObserver`**    | Abstract Class | The interface for the **Observer Pattern**. Defines the `update` method.                                                                                       |
| **`Scoreboard`**      | Concrete Class | A concrete observer that subscribes to the `Game` and updates scores when notified.                                                                            |
| **`TicTacToeDemo`**   | Class          | Contains the application entry point (`main` method) to simulate multiple games.                                                                               |

### Enumerations

| Enumeration      | Definition                                                                                        |
| :--------------- | :------------------------------------------------------------------------------------------------ |
| **`GameStatus`** | Defines the possible high-level states of a game (`IN_PROGRESS`, `WINNER_X`, `WINNER_O`, `DRAW`). |
| **`Symbol`**     | Defines the marks that can be placed on the board (`X`, `O`) and the empty-cell marker (`T`).     |
