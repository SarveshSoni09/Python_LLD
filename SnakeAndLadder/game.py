from board_entity import BoardEntity
from board import Board
from player import Player
from dice import Dice
from typing import List
from collections import deque
from game_status import GameStatus


class Game:
    """
    CONTEXT: The central class that manages the overall game state and flow.
    It coordinates interactions between Player, Board, and Dice.
    """

    class Builder:
        """
        BUILDER PATTERN: Provides a fluent, step-by-step, and controlled way
        to construct a complex Game object, ensuring all required components are set
        before instantiation. This improves readability and setup robustness.
        """

        def __init__(self):
            self.board = None
            self.players = None
            self.dice = None

        def set_board(self, board_size: int, board_entities: List[BoardEntity]):
            # Builder handles the creation of the complex component (Board).
            self.board = Board(board_size, board_entities)
            return self

        def set_players(self, player_names: List[str]):
            # Builder handles the collection of Player objects using a deque (optimized for game turns).
            self.players = deque()
            for player_name in player_names:
                self.players.append(Player(player_name))
            return self

        def set_dice(self, dice: Dice):
            self.dice = dice
            return self

        def build(self):
            # Validation: Ensures all required components are set before returning the Game object.
            if self.board is None or self.players is None or self.dice is None:
                raise ValueError("Board, Payers, and Dice must be set.")
            return Game(
                self
            )  # Passes itself (the fully configured builder) to the Game constructor.

    def __init__(self, builder: "Game.Builder"):
        # Encapsulation: Game instance is initialized using the immutable state from the Builder.
        self.board = builder.board
        self.players = builder.players
        self.dice = builder.dice
        self.status = GameStatus.NOT_STARTED
        self.winner = None

    def play(self):
        """Manages the main game loop."""
        if len(self.players) < 2:
            print("Cannot start a game. At least 2 players needed.")
            return

        self.status = GameStatus.RUNNING
        print("Game started!")

        while self.status == GameStatus.RUNNING:
            # Data Structure Use: deque is used for efficient player rotation (O(1) popleft/append).
            current_player = self.players.popleft()
            self.take_turn(current_player)

            if self.status == GameStatus.RUNNING:
                self.players.append(current_player)  # Rotate the player queue

        # Final output logic
        print("Game finished!")
        if self.winner is not None:
            print(f"The winner is {self.winner.get_name()}!")

    def take_turn(self, player: Player):
        """Handles a single player's turn, including movement, entity checks, and extra rolls."""
        roll = self.dice.roll()
        print(f"\n{player.get_name()}'s turn. Rolled a {roll}.")

        current_position = player.get_position()
        next_position = current_position + roll

        # Rule 1: Overshooting the final box.
        if next_position > self.board.get_size():
            print(
                f"Over roll! {player.get_name()} is at position {player.get_position()} and needs to land exactly on {self.board.get_size()}. Turn skipped."
            )
            return

        # Rule 2: Landing exactly on the final box.
        if next_position == self.board.get_size():
            player.set_position(next_position)
            self.winner = player
            self.status = GameStatus.FINISHED
            print(
                f"Winner Winner Chicken Dinner! {player.get_name()} reached the final box {self.board.get_size()} and won."
            )
            return

        # Rule 3: Landing on a snake, ladder, or normal square.
        # Abstraction: Asks the Board for the final position, hiding entity lookup.
        final_position = self.board.get_final_position(next_position)

        # Print descriptive messages based on the movement type.
        if final_position > next_position:
            print(
                f"Wow! {player.get_name()} found a Ladder at {next_position} and climbed to {final_position}."
            )
        elif final_position < next_position:
            print(
                f"Damn! {player.get_name()} was bitten by a Snake at {next_position} and slid down to {final_position}."
            )
        else:
            print(
                f"{player.get_name()} moved from {current_position} to {final_position}."
            )

        player.set_position(final_position)

        # Rule 4: Extra turn on rolling a 6. Recursively calls take_turn.
        if roll == self.dice.max_val:
            print(
                f"{player.get_name()} has rolled a {self.dice.max_val} and gets another turn!"
            )
            self.take_turn(player)
