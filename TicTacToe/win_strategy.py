from abc import ABC, abstractmethod
from board import Board
from player import Player


class WinStrategy:
    @abstractmethod
    def check_winner(self, board: Board, player: Player) -> bool:
        pass


class RowWinningStrategy(WinStrategy):
    def check_winner(self, board: Board, player: Player) -> bool:
        pass


class ColWinningStrategy(WinStrategy):
    def check_winner(self, board: Board, player: Player) -> bool:
        pass


class DiagonalWinningStrategy(WinStrategy):
    def check_winner(self, board: Board, player: Player) -> bool:
        pass
