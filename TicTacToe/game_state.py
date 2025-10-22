from abc import ABC, abstractmethod
from player import Player
from invalid_move_exception import InvalidMoveException
from enums import GameStatus, Symbol


class GameState(ABC):
    @abstractmethod
    def handle_move(self, game, player: Player, row: int, col: int):
        pass


class InProgressState(GameState):
    def handle_move(self, game, player: Player, row: int, col: int):
        if game.get_current_player() != player:
            raise InvalidMoveException("Not your turn!")

        game.get_board().place_symbol(row, col, player.get_symbol())

        if game.check_winner(player):
            game.set_winner(player)
            game.set_status(
                GameStatus.WINNER_X
                if player.get_symbol() == Symbol.X
                else GameStatus.WINNER_O
            )
            game.set_state(WinnerState())
        elif game.get_board().is_full():
            game.set_status(GameStatus.DRAW)
            game.set_state(DrawState())
        else:
            game.switch_player()


class DrawState(GameState):
    def handle_move(self, game, player: Player, row: int, col: int):
        raise InvalidMoveException("Game is already over. It was a draw.")


class WinnerState(GameState):
    def handle_move(self, game, player: Player, row: int, col: int):
        raise InvalidMoveException(
            f"Game is already over. {game.get_winner().get_name()} has won."
        )
