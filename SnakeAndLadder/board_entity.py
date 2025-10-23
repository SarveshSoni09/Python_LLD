from abc import ABC


class BoardEntity(ABC):
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def get_start(self) -> int:
        return self.start

    def get_end(self) -> int:
        return self.end


class Snake(BoardEntity):
    def __init__(self, start: int, end: int):
        super().__init__(start, end)
        if start <= end:
            raise ValueError("Snakes' head must be at a higher position than its tail.")


class Ladder(BoardEntity):
    def __init__(self, start: int, end: int):
        super().__init__(start, end)
        if start >= end:
            raise ValueError(
                "Ladders' bottom must be at a lower position than its top."
            )
