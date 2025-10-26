from board_entity import Snake, Ladder
from game import Game
from dice import Dice


class GameDemo:
    """
    CLIENT: Demonstrates how the system is assembled and run.
    It interacts with the Game object using its public API (Builder and play()).
    """

    @staticmethod
    def main():
        # LLD: Defining game entities separately from the Board, promoting SRP.
        board_entities = [
            # Snake and Ladder objects self-validate their start/end positions upon creation.
            Snake(17, 7),
            Snake(54, 34),
            Snake(62, 19),
            Snake(98, 79),
            Ladder(3, 38),
            Ladder(24, 33),
            Ladder(42, 93),
            Ladder(72, 84),
        ]

        players = ["Parzival", "Art3mis", "PlaidT"]

        # Builder Pattern in action: Fluent interface for configuration.
        game = (
            Game.Builder()
            .set_board(100, board_entities)
            .set_players(players)
            .set_dice(Dice(1, 6))  # Using the Dice interface.
            .build()
        )

        game.play()


if __name__ == "__main__":
    GameDemo.main()
