from abc import abstractmethod
from typing import List, Tuple, NamedTuple
from os import path

from .cli import Game


here = path.abspath(path.dirname(__file__))
DEFAULT_WORD_FILE = path.join(here, 'words', 'words.txt')


class Word(NamedTuple):
    word: str
    path: List[Tuple[int, int]]


class WordReader(object):
    """
    Read list of words from a file.
    """
    @staticmethod
    def read_from_file(file_name: str) -> List[str]:
        with open(file_name, 'r') as f:
            words = f.readlines()
        return words


class Node(object):
    def __init__(self, value: str):
        self.value = value
        self.children: List[Node] = []


class NodeBoard(object):
    def __init__(self, game: Game):
        self.nodes = NodeBoardBuilder(game).build()

    def __iter__(self):
        self.i = 0
        self.j = -1
        return self

    def __next__(self):
        if self.j < Game.WIDTH - 1:
            self.j += 1
            result = self.nodes[self.i][self.j]
            return result
        elif self.i < Game.HEIGHT - 1:
            self.j = 0
            self.i += 1
            result = self.nodes[self.i][self.j]
            return result
        else:
            raise StopIteration


class NodeBoardBuilder(object):
    """
    A game where every cell is linked to each other
    """

    def __init__(self, game: Game):
        self.game = game

    def build(self) -> List[List[Node]]:
        nodes = self._create_nodes()
        return self._link_nodes(nodes)

    def _create_nodes(self) -> List[List[Node]]:
        """
        Creates Nodes from board cells.
        """
        all_nodes = []
        for i in range(Game.WIDTH):
            node_row = []
            for j in range(Game.HEIGHT):
                node = Node(self.game[i, j])
                node_row.append(node)
            all_nodes.append(node_row)
        return all_nodes

    def _link_nodes(self, nodes):
        """
        Links all created nodes to each other.
        """
        for i in range(Game.WIDTH):
            for j in range(Game.HEIGHT):
                self._link_adjacent_nodes(nodes, i, j)
        return nodes

    def _link_adjacent_nodes(self, nodes, i, j):
        """
        Links adjacent nodes of node in index i, j to each other.
        """
        for x, y in self._adjacent_indices(i, j):
            try:
                self._link_two_adjacent_nodes(nodes[i][j], nodes[x][y])
            except IndexError:
                pass

    def _link_two_adjacent_nodes(self, node: Node, adjacent_node: Node):
        node.children.append(adjacent_node)

    def _adjacent_indices(self, i: int, j: int) -> List[Tuple[int, int]]:
        return [
            (i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1),
            (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)
        ]


class Solver(object):
    """
    Solves a game.
    """

    def __init__(self) -> None:
        self.possible_words = WordReader.read_from_file(
            DEFAULT_WORD_FILE
        )

    @abstractmethod
    def solve(self, game: Game) -> List[str]:
        pass


class SimpleSolver(Solver):

    def solve(self, game: Game) -> List[str]:
        board = game.board
        if (board[0][0] + board[0][1] + board[0][2] == "hei"):
            return ["hei"]
        return []


class NodeSolver(Solver):

    def solve(self, game: Game) -> List[str]:
        nodes = NodeBoard(game)
        found_words = []
        for node in nodes:
            new_words = self.traverse_starting_from_node(node)
            found_words += new_words
        return found_words

    def traverse_starting_from_node(self, node: Node) -> List[str]:
        return []
