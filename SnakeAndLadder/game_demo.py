from board_entity import Snake, Ladder
from game import Game
from dice import Dice


class GameDemo:
    @staticmethod
    def main():
        board_entities = [
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

        game = (
            Game.Builder()
            .set_board(100, board_entities)
            .set_players(players)
            .set_dice(Dice(1, 6))
            .build()
        )

        game.play()


if __name__ == "__main__":
    GameDemo.main()
