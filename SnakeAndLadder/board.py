from board_entity import BoardEntity
from typing import List


class Board:
    """
    SRP: Responsible only for the board's structure and entity configuration.
    It does not contain player or game logic.

    COMPOSITION: Board HAS-A collection of BoardEntity objects (though stored in a dict).
    """

    def __init__(self, size: int, entities: List[BoardEntity]):
        self.size = size
        # Data Structure Choice: Using a dictionary for O(1) lookup of snake/ladder starts.
        self.snakes_and_ladders = {}

        for entity in entities:
            # Encapsulation: Populates the lookup table using the entity's start and end accessors.
            self.snakes_and_ladders[entity.get_start()] = entity.get_end()

    def get_size(self) -> int:
        return self.size

    def get_final_position(self, position: int) -> int:
        """
        ABSTRACTION: Hides the underlying complexity of checking for a snake or ladder.
        The Game class only asks for the 'final' position, unaware if it moved or not.
        """
        # Dictionary.get() provides a default value (the current position) if no entity exists.
        return self.snakes_and_ladders.get(position, position)
