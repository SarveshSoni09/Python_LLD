from cell import Cell
from enums import Symbol
from invalid_move_exception import InvalidMoveException


class Board:
    """
    SINGLE RESPONSIBILITY PRINCIPLE (SRP):
    The Board class is responsible ONLY for managing the grid's state (data structure)
    and enforcing simple boundary/occupancy rules. It does NOT contain game logic
    (like checking for a winner or switching players).

    ENCAPSULATION:
    The internal 'board' list of lists and 'moves_count' are protected by public
    methods like place_symbol, is_full, and get_cell.
    """

    def __init__(self, size: int):
        self.size = size
        self.moves_count = 0
        self.board = []
        self.initialize_board()

    def initialize_board(self):
        # Initializing the board with Cell objects instead of raw symbols
        # is an excellent example of Composition (Board HAS-A collection of Cells).
        for row in range(self.size):
            board_row = []
            for col in range(self.size):
                board_row.append(
                    Cell()
                )  # Each position is an encapsulated Cell object.
            self.board.append(board_row)

    def place_symbol(self, row: int, col: int, symbol: Symbol) -> bool:
        # Input Validation: Ensures robustness by throwing custom exceptions.
        if row < 0 or col < 0 or row >= self.size or col >= self.size:
            raise InvalidMoveException(" Invalid Position: Out of bounds.")

        # Check occupancy via the Cell's encapsulated method.
        if self.board[row][col].get_symbol() != Symbol.T:
            raise InvalidMoveException("Invalid Move: Cell already filled.")

        self.board[row][col].set_symbol(symbol)
        self.moves_count += 1
        return True

    def get_cell(self, row: int, col: int):
        # Defensive Programming: Returns None for out-of-bounds access.
        if row < 0 or col < 0 or row >= self.size or col >= self.size:
            return None
        return self.board[row][col]

    def is_full(self) -> bool:
        # Efficient check by comparing move count to total cells.
        return self.moves_count == self.size**2

    def print_board(self):
        # Abstraction: Provides a clean visual representation of the internal state.
        print("------------")
        for i in range(self.size):
            print("| ", end="")
            for j in range(self.size):
                symbol = self.board[i][j].get_symbol()
                print(f"{symbol.get_char()} | ", end="")
            print("\n------------")

    def get_size(self) -> int:
        return self.size
