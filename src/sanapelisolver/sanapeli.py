"""
Solves a game
"""

from collections import namedtuple
from enum import Enum
from os import path
from typing import List

here = path.abspath(path.dirname(__file__))
DEFAULT_WORD_FILE = path.join(here, 'words', 'words.txt')


class InputError(Exception):
    pass


class GameSize(Enum):
    HEIGHT = 4
    WIDTH = 4


class Word(namedtuple('Word', ['word', 'path'])):
    pass


class Game(object):
    """
    Respresents a game.
    """

    def __init__(self, board: List[List[str]]):
        self.board: List[List[str]] = board
        self.words = None

    def __str__(self) -> str:
        string = "---------\n"
        for line in self.board:
            string += "|" + "|".join(line) + "|\n"
        string += "---------\n"
        return string.upper()


class Solver(object):
    """
    Solves a game.
    """

    def __init__(self, possible_words: List[str]) -> None:
        self.possible_words = possible_words

    def solve(self, game: Game) -> List[str]:
        return ["not", "actual", "answer"]


class WordReader(object):
    """
    Read list of words from a file.
    """
    @staticmethod
    def read_from_file(file_name: str) -> List[str]:
        with open(file_name, 'r') as f:
            words = f.readlines()
        return words


class GameReader(object):
    """
    Read a game.
    """
    @staticmethod
    def read_from_cmd_line() -> List[List[str]]:
        """
        Read a game from command line like this:
        rfrf
        gggg
        hhhh
        thyh
        """
        board = []
        for i in range(GameSize.HEIGHT.value):
            line = list(input())
            if len(line) != GameSize.WIDTH.value:
                raise InputError
            board.append(line)
        return board


def main():
    print("SANAPELI RATKAISIJA: Anna peli")
    board = GameReader.read_from_cmd_line()
    game = Game(board)
    existing_words = WordReader.read_from_file(DEFAULT_WORD_FILE)
    Solver(existing_words).solve(game)
    print(str(game))


if __name__ == "__main__":
    main()
