from board_entity import BoardEntity
from board import Board
from player import Player
from dice import Dice
from typing import List
from collections import deque
from game_status import GameStatus


class Game:
    class Builder:
        def __init__(self):
            self.board = None
            self.players = None
            self.dice = None

        def set_board(self, board_size: int, board_entities: List[BoardEntity]):
            self.board = Board(board_size, board_entities)
            return self

        def set_players(self, player_names: List[str]):
            self.players = deque()
            for player_name in player_names:
                self.players.append(Player(player_name))
            return self

        def set_dice(self, dice: Dice):
            self.dice = dice
            return self

        def build(self):
            if self.board is None or self.players is None or self.dice is None:
                raise ValueError("Board, Payers, and Dice must be set.")
            return Game(self)

    def __init__(self, builder: "Game.Builder"):
        self.board = builder.board
        self.players = builder.players
        self.dice = builder.dice
        self.status = GameStatus.NOT_STARTED
        self.winner = None

    def play(self):
        if len(self.players) < 2:
            print("Cannot start a game. At least 2 players needed.")
            return

        self.status = GameStatus.RUNNING
        print("Game started!")

        while self.status == GameStatus.RUNNING:
            current_player = self.players.popleft()
            self.take_turn(current_player)

            if self.status == GameStatus.RUNNING:
                self.players.append(current_player)

        print("Game finished!")
        if self.winner is not None:
            print(f"The winner is {self.winner.get_name()}!")

    def take_turn(self, player: Player):
        roll = self.dice.roll()
        print(f"\n{player.get_name()}'s turn. Rolled a {roll}.")

        current_position = player.get_position()
        next_position = current_position + roll

        if next_position > self.board.get_size():
            print(
                f"Over roll! {player.get_name()} is at position {player.get_position()} and needs to land exactly on {self.board.get_size()}. Turn skipped."
            )
            return

        if next_position == self.board.get_size():
            player.set_position(next_position)
            self.winner = player
            self.status = GameStatus.FINISHED
            print(
                f"Winner Winner Chicken Dinner! {player.get_name()} reached the final box {self.board.get_size()} and won."
            )
            return

        final_position = self.board.get_final_position(next_position)

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

        if roll == 6:
            print(f"{player.get_name()} has rolled a 6 and gets another turn!")
            self.take_turn(player)
