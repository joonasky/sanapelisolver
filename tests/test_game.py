from unittest import TestCase
from mock import patch

from src.sanapeli import GameReader, InputError, Game, Solver


class TestGameReader(TestCase):

    def test_read_from_cmd_line_proper_input(self):
        user_input = [
            'abcd',
            'efgh',
            'ijkl',
            'mnoq'
        ]
        expected_game = [
            ['a', 'b', 'c', 'd'],
            ['e', 'f', 'g', 'h'],
            ['i', 'j', 'k', 'l'],
            ['m', 'n', 'o', 'q']
        ]
        with patch('builtins.input', side_effect=user_input):
            game = GameReader().read_from_cmd_line()
        self.assertEqual(game, expected_game)

    def test_read_from_cmd_line_improper_input(self):
        user_input = [
            'abcdq',
            'efg',
            'asd'
        ]

        with patch('builtins.input', side_effect=user_input):
            with self.assertRaises(InputError):
                GameReader().read_from_cmd_line()

    def test_solver(self):
        board = [
            ['h', 'i', 'l', 'l'],
            ['e', 'f', 'a', 'h'],
            ['i', 'l', 'l', 'n'],
            ['m', 'n', 'e', 'q']
        ]
        game = Game(board)
        solved_game = Solver(MockWordReader()).solve(game)


class MockWordReader(object):
    @staticmethod
    def read():
        return ["hei", "illallinen"]
