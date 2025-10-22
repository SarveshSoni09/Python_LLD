import threading
from scoreboard import Scoreboard
from player import Player
from game import Game
from invalid_move_exception import InvalidMoveException


class TicTacToe:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if not hasattr(self, "initialized"):
            self.game = None
            self.scoreboard = Scoreboard()
            self.initialized = True

    @classmethod
    def get_instance(cls):
        return cls()

    def create_game(self, player1: Player, player2: Player):
        self.game = Game(player1, player2)
        self.game.add_observer(self.scoreboard)
        print(
            f"Game started between {player1.get_name()} (X) and {player2.get_name()} (O)."
        )

    def make_move(self, player: Player, row: int, col: int):
        if self.game is None:
            print("No game in progress. Please create a game first.")
            return

        try:
            print(f"{player.get_name()} plays at ({row}, {col})")
            self.game.make_move(player, row, col)
            self.print_board()
            print(f" Game Status: {self.game.get_status().value}")
            if self.game.get_winner() is not None:
                print(f"Winner: {self.game.get_winner().get_name()}")
        except InvalidMoveException as e:
            print(f"Error: {e}")

    def print_board(self):
        self.game.get_board().print_board()

    def print_scoreboard(self):
        self.scoreboard.print_scores()
