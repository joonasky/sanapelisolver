from unittest import TestCase
from unittest.mock import patch

from sanapelisolver.cli import InteractiveGameReader, InputError, Game
from sanapelisolver.solver import SimpleSolver, WordReader


class TestGameReader(TestCase):

    def test_read_from_cmd_line_proper_input(self):
        user_input = [
            'abcd',
            'efgh',
            'ijkl',
            'mnoq'
        ]
        expected_game = Game([
            ['a', 'b', 'c', 'd'],
            ['e', 'f', 'g', 'h'],
            ['i', 'j', 'k', 'l'],
            ['m', 'n', 'o', 'q']
        ])
        with patch('builtins.input', side_effect=user_input):
            game = InteractiveGameReader().read_game()
        self.assertEqual(game.board, expected_game.board)

    def test_read_from_cmd_line_improper_input(self):
        user_input = [
            'abcdq',
            'efg',
            'asd'
        ]

        with patch('builtins.input', side_effect=user_input):
            with self.assertRaises(InputError):
                InteractiveGameReader().read_game()

    @patch.object(WordReader, "read_from_file")
    def test_solver(self, mock_method):
        board = [
            ['h', 'i', 'l', 'l'],
            ['e', 'f', 'a', 'h'],
            ['i', 'l', 'l', 'n'],
            ['m', 'n', 'e', 'q']
        ]
        game = Game(board)
        SimpleSolver().solve(game)
