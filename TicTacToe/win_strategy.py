from abc import ABC, abstractmethod
from board import Board
from player import Player


class WinStrategy(ABC):
    """
    STRATEGY INTERFACE: Defines the common interface for all winning conditions. (LSP)
    """

    def __init__(self):
        # Added to satisfy standard Python inheritance practice.
        pass

    @abstractmethod
    def check_winner(self, board: Board, player: Player) -> bool:
        pass


class RowWinningStrategy(WinStrategy):
    """
    CONCRETE STRATEGY: Implements the check for a win across any row.
    """

    def __init__(self):
        super().__init__()

    def check_winner(self, board: Board, player: Player) -> bool:
        # Logic is self-contained and focused ONLY on rows (SRP).
        for row in range(board.get_size()):
            row_win = True
            for col in range(board.get_size()):
                if board.get_cell(row, col).get_symbol() != player.get_symbol():
                    row_win = False
                    break
            if row_win:
                return True
        return False


class ColWinningStrategy(WinStrategy):
    """
    CONCRETE STRATEGY: Implements the check for a win across any column.
    """

    def __init__(self):
        super().__init__()

    def check_winner(self, board: Board, player: Player) -> bool:
        # Logic is self-contained and focused ONLY on columns (SRP).
        for col in range(board.get_size()):
            col_win = True
            for row in range(board.get_size()):
                if board.get_cell(row, col).get_symbol() != player.get_symbol():
                    col_win = False
                    break
            if col_win:
                return True
        return False


class DiagonalWinningStrategy(WinStrategy):
    """
    CONCRETE STRATEGY: Implements the check for a win along both main diagonals.
    """

    def __init__(self):
        super().__init__()

    def check_winner(self, board: Board, player: Player) -> bool:
        # Logic is self-contained and focused ONLY on diagonals (SRP).

        # Check main diagonal (top-left to bottom-right)
        diag_win = True
        for i in range(board.get_size()):
            if board.get_cell(i, i).get_symbol() != player.get_symbol():
                diag_win = False
                break
        if diag_win:
            return True

        # Check anti-diagonal (top-right to bottom-left)
        anti_diag_win = True
        for i in range(board.get_size()):
            if (
                board.get_cell(i, board.get_size() - 1 - i).get_symbol()
                != player.get_symbol()
            ):
                anti_diag_win = False
                break
        return anti_diag_win
