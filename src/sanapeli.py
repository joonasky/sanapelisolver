from collections import namedtuple
from enum import Enum


class InputError(Exception):
    pass


class GameSize(Enum):
    HEIGHT = 4
    WIDTH = 4


class Word(namedtuple('Word', ['word', 'path'])):
    pass


class Game(object):
    def __init__(self, board):
        self.board = board
        self.words = None
    
    def __str__(self):
        string = "-----------\n"
        for line in self.board:
            string += "|" + "|".join(line) + "|\n"
        string += "-----------\n"
        return string.upper()


class Solver(object):
    def __init__(self, word_reader):
        self.possible_words = word_reader.read()

    def solve(self, game):
        return game


class WordReader(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        with open(self.file_name, 'r') as f:
            words = f.readlines()
        return words


class GameReader(object):

    @staticmethod
    def read_from_cmd_line():
        board = []
        for i in range(GameSize.HEIGHT.value):
            line = list(input())
            if len(line) != GameSize.WIDTH.value:
                raise InputError
            board.append(line)
        return board


if __name__ == "__main__":
    print("SANAPELI RATKAISIJA: Anna peli")
    board = GameReader().read_from_cmd_line()
    print("------------------------------")
    game = Game(board)
    solved_game = Solver(WordReader("words/words.txt")).solve(game)
    print(str(game))
