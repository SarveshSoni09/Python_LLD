from enums import Symbol


class Cell:
    def __init__(self):
        self.symbol = Symbol.T

    def get_symbol(self) -> Symbol:
        return self.symbol

    def set_symbol(self, symbol: Symbol):
        self.symbol = symbol
