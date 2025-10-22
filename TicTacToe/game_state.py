from abc import ABC, abstractmethod
from player import Player
from invalid_move_exception import InvalidMoveException
from enums import GameStatus, Symbol


class GameState(ABC):
    """
    STATE INTERFACE: Defines the contract (handle_move) for all possible game states.
    This enables Polymorphism: the Game class can call handle_move regardless of the
    current state object.
    """

    @abstractmethod
    def handle_move(self, game, player: Player, row: int, col: int):
        pass


class InProgressState(GameState):
    """
    CONCRETE STATE: Contains all logic relevant to a game actively being played.
    It is responsible for enforcing turn order, handling a move, checking for win/draw,
    and triggering state transitions.
    """

    def handle_move(self, game, player: Player, row: int, col: int):
        if game.get_current_player() != player:
            raise InvalidMoveException("Not your turn!")

        # Delegation: The state uses the context (game) to interact with the Board.
        game.get_board().place_symbol(row, col, player.get_symbol())

        if game.check_winner(player):
            # State Transition: InProgress -> WinnerState
            game.set_winner(player)
            game.set_status(
                GameStatus.WINNER_X
                if player.get_symbol() == Symbol.X
                else GameStatus.WINNER_O
            )
            game.set_state(WinnerState())
        elif game.get_board().is_full():
            # State Transition: InProgress -> DrawState
            game.set_status(GameStatus.DRAW)
            game.set_state(DrawState())
        else:
            game.switch_player()


class DrawState(GameState):
    """
    CONCRETE STATE: Game is finished in a draw.
    It enforces the rule that no further moves are allowed.
    """

    def handle_move(self, game, player: Player, row: int, col: int):
        raise InvalidMoveException("Game is already over. It was a draw.")


class WinnerState(GameState):
    """
    CONCRETE STATE: Game is finished with a winner.
    It enforces the rule that no further moves are allowed.
    """

    def handle_move(self, game, player: Player, row: int, col: int):
        raise InvalidMoveException(
            f"Game is already over. {game.get_winner().get_name()} has won."
        )
