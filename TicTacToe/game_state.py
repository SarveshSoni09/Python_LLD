from abc import ABC, abstractmethod
from player import Player


class GameState(ABC):
    @abstractmethod
    def handle_move(self, game, player: Player, row: int, col: int):
        pass


class InProgressState(GameState):
    def handle_move(self, game, player: Player, row: int, col: int):
        pass


class DrawState(GameState):
    def handle_move(self, game, player: Player, row: int, col: int):
        pass


class WinnerState(GameState):
    def handle_move(self, game, player: Player, row: int, col: int):
        pass
