from cell import Cell
from enums import Symbol
from invalid_move_exception import InvalidMoveException


class Board:
    def __init__(self, size: int):
        self.size = size
        self.moves_count = 0
        self.board = []
        self.initialize_board()

    def initialize_board(self):
        for row in range(self.size):
            board_row = []
            for col in range(self.size):
                board_row.append(Cell())
            self.board.append(board_row)

    def place_symbol(self, row: int, col: int, symbol: Symbol) -> bool:
        if row < 0 or col < 0 or row >= self.size or col >= self.size:
            raise InvalidMoveException(" Invalid Position: Out of bounds.")
        if self.board[row][col].get_symbol() != Symbol.T:
            raise InvalidMoveException("Invalid Move: Cell already filled.")

        self.board[row][col].set_symbol(symbol)
        self.moves_count += 1
        return True

    def get_cell(self, row: int, col: int):
        if row < 0 or col < 0 or row >= self.size or col >= self.size:
            return None
        return self.board[row][col]

    def is_full(self) -> bool:
        return self.moves_count == self.size**2

    def print_board(self):
        print("----------")
        for i in range(self.size):
            print("| ", end="")
            for j in range(self.size):
                symbol = self.board[i][j].get_symbol()
                print(f"{symbol.get_char()} | ", end="")
            print("\n----------")

    def get_size(self) -> int:
        return self.size
