from abc import ABC, abstractmethod
from typing import List


Board = List[List[str]]


class Game(object):
    """
    Respresents a game.
    """

    HEIGHT = 4
    WIDTH = 4

    def __init__(self, board: Board):
        self.board = board

    def __getitem__(self, indices):
        return self.board[indices[0]][indices[1]]

    def __str__(self) -> str:
        string = "---------\n"
        for line in self.board:
            string += "|" + "|".join(line) + "|\n"
        string += "---------\n"
        return string.upper()


class InputError(Exception):
    pass


class GameReader(ABC):
    """
    User interface.
    """

    @abstractmethod
    def read_game(self) -> Game:
        """
        Method for reading a game from wanted source.
        """
        pass


class InteractiveGameReader(GameReader):
    """
    Read a game from command line through input
    """

    def read_game(self) -> Game:
        board = []
        for i in range(Game.HEIGHT):
            line = list(input())
            if len(line) != Game.WIDTH:
                raise InputError
            board.append(line)
        return Game(board)


class CommandLineGameReader(GameReader):
    """
    Read a game from command line through commandl ine arguments.
    """

    def __init__(self, cmd_line_arguments):
        super().__init__()
        self.args = cmd_line_arguments

    def read_game(self) -> Game:
        board = []
        x = 0
        for i in range(Game.HEIGHT):
            line = self.args[x]
            x += 1
            if len(line) != Game.WIDTH:
                raise InputError
            board.append(line)
        return Game(board)
