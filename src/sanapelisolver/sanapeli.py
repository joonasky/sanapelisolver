"""
Solves a game
"""

from .cli import InteractiveGameReader
from .solver import SimpleSolver


def main():
    game = InteractiveGameReader().read_game()
    print(str(game))
    solution = SimpleSolver().solve(game)
    print(solution)


if __name__ == "__main__":
    main()
