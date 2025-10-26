from abc import ABC


class BoardEntity(ABC):
    """
    ABSTRACT BASE CLASS (LSP): Defines the common contract for all entities (Snakes and Ladders).
    All entities must have a start and an end position.
    """

    def __init__(self, start: int, end: int):
        # Encapsulation: The state (start/end) is protected within the entity.
        self.start = start
        self.end = end

    def get_start(self) -> int:
        return self.start

    def get_end(self) -> int:
        return self.end


class Snake(BoardEntity):
    """
    CONCRETE ENTITY: Represents a Snake.
    INHERITANCE: Inherits structure from BoardEntity.

    The constructor includes crucial domain validation to enforce
    the rule that a snake's end must be less than its start (sliding down).
    """

    def __init__(self, start: int, end: int):
        super().__init__(start, end)
        if start <= end:
            # Throws an exception for invalid game setup.
            raise ValueError("Snakes' head must be at a higher position than its tail.")


class Ladder(BoardEntity):
    """
    CONCRETE ENTITY: Represents a Ladder.
    INHERITANCE: Inherits structure from BoardEntity.

    The constructor includes domain validation to enforce
    the rule that a ladder's end must be greater than its start (climbing up).
    """

    def __init__(self, start: int, end: int):
        super().__init__(start, end)
        if start >= end:
            # Ensures valid game state upon object creation.
            raise ValueError(
                "Ladders' bottom must be at a lower position than its top."
            )
