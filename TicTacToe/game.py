from game_subject import GameSubject
from player import Player
from board import Board
from enums import GameStatus
from game_state import GameState
from game_state import InProgressState
from win_strategy import RowWinningStrategy, ColWinningStrategy, DiagonalWinningStrategy


class Game(GameSubject):
    """
    CONTEXT (State Pattern): Holds the current state object and delegates 'make_move'.
    SUBJECT (Observer Pattern): Maintains a list of observers (Scoreboard) and notifies them
    when the game status changes to final (Win/Draw).
    CONTEXT (Strategy Pattern): Holds the list of WinStrategy objects and uses them
    in check_winner. This allows for easy addition of new win conditions (OCP).
    """

    def __init__(self, player1: Player, player2: Player):
        super().__init__()
        self.board = Board(3)  # Composition: Game HAS-A Board.
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.winner = None
        self.status = GameStatus.IN_PROGRESS
        self.state = InProgressState()  # Initial state is InProgressState.

        # Strategy Pattern: Strategy objects are instantiated and held by the Context (Game).
        self.winning_strategies = [
            RowWinningStrategy(),
            ColWinningStrategy(),
            DiagonalWinningStrategy(),
        ]

    def make_move(self, player: Player, row: int, col: int):
        # Delegation: Delegates the core logic to the current state object. (State Pattern)
        self.state.handle_move(self, player, row, col)

    def check_winner(self, player: Player) -> bool:
        # Strategy Pattern: Iterates through strategies and delegates the win check.
        for strategy in self.winning_strategies:
            # Polymorphism: Calls the check_winner method without knowing the concrete strategy.
            if strategy.check_winner(self.board, player):
                return True

        return False

    def switch_player(self):
        self.current_player = (
            self.player2 if self.current_player == self.player1 else self.player1
        )

    # Getter methods for encapsulated attributes
    def get_board(self):
        return self.board

    def get_current_player(self):
        return self.current_player

    def get_winner(self):
        return self.winner

    def set_winner(self, winner: Player):
        self.winner = winner

    def get_status(self):
        return self.status

    def set_status(self, status: GameStatus):
        self.status = status
        if status != GameStatus.IN_PROGRESS:
            # Observer Pattern: Notifies observers (Scoreboard) upon game completion.
            self.notify_observers()

    def set_state(self, state: GameState):
        # Context's method to change the state.
        self.state = state
