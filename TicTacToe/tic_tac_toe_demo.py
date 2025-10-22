from tic_tac_toe import TicTacToe
from player import Player
from enums import Symbol


class TicTacToeDemo:
    @staticmethod
    def main():
        game = TicTacToe.get_instance()
        p1 = Player("Parzival", Symbol.X)
        p2 = Player("Art3mis", Symbol.O)

        print("--- Game 1: Parzival (X) vs Art3mis (O) ---")
        game.create_game(p1, p2)
        game.print_board()
        game.make_move(p1, 0, 0)
        game.make_move(p2, 1, 0)
        game.make_move(p1, 0, 1)
        game.make_move(p2, 1, 1)
        game.make_move(p1, 0, 2)
        print("-------------------------------------------")

        print("--- Game 2: Parzival (X) vs Art3mis (O) ---")
        game.create_game(p1, p2)
        game.print_board()
        game.make_move(p1, 0, 0)
        game.make_move(p2, 1, 0)
        game.make_move(p1, 0, 1)
        game.make_move(p2, 1, 1)
        game.make_move(p1, 2, 2)
        game.make_move(p2, 1, 2)
        print("-------------------------------------------")

        print("--- Game 3: Parzival (X) vs Art3mis (O) ---")
        game.create_game(p1, p2)
        game.print_board()
        game.make_move(p1, 0, 0)
        game.make_move(p2, 0, 1)
        game.make_move(p1, 0, 2)
        game.make_move(p2, 1, 1)
        game.make_move(p1, 1, 0)
        game.make_move(p2, 1, 2)
        game.make_move(p1, 2, 1)
        game.make_move(p2, 2, 0)
        game.make_move(p1, 2, 2)
        print("-------------------------------------------")

        game.print_scoreboard()

        print("--- Testing edge-cases ---")
        game.create_game(p1, p2)
        game.print_board()
        game.make_move(p1, 0, 0)
        game.make_move(p1, 0, 1)
        game.make_move(p2, 0, 1)
        game.make_move(p1, 0, 2)
        game.make_move(p2, 0, 0)
        game.make_move(p2, 1, 0)
        game.make_move(p1, 1, 1)
        game.make_move(p2, 2, 0)
        game.make_move(p1, 2, 2)
        game.make_move(p2, 2, 1)
        print("-------------------------------------------")


if __name__ == "__main__":
    TicTacToeDemo.main()
