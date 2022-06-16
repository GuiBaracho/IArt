# takuzu.py: Template para implementação do projeto de Inteligência Artificial 2021/2022.
# Devem alterar as classes e funções neste ficheiro de acordo com as instruções do enunciado.
# Além das funções e classes já definidas, podem acrescentar outras que considerem pertinentes.

# Grupo 00:
# 00000 Nome1
# 00000 Nome2

from ctypes import sizeof
import sys
from types import NoneType
from search import (
    Problem,
    Node,
    astar_search,
    breadth_first_tree_search,
    depth_first_tree_search,
    greedy_search,
    recursive_best_first_search,
)


class TakuzuState:
    state_id = 0

    def __init__(self, board):
        self.board = board
        self.id = TakuzuState.state_id
        TakuzuState.state_id += 1

    def __lt__(self, other):
        return self.id < other.id

    # Outros metodos da classe

    def bd(self):
        return self.board


class Board:
    def __init__(self, content) -> None:
        """Representação interna de um tabuleiro de Takuzu."""

        content = content.split('\n')
        n = int(content[0])
        board = content[1:(n + 1)]
        for i in range(n):
            board[i] = board[i].split('\t')
            board[i] = [int(x) for x in board[i]]

        self.s = n
        self.l = board

    def get_number(self, row: int, col: int) -> int:
        """Devolve o valor na respetiva posição do tabuleiro."""
        return self.l[row][col]

    def adjacent_vertical_numbers(self, row: int, col: int):
        """Devolve os valores imediatamente abaixo e acima,
        respectivamente."""
        up = None
        down = None
        if(row - 1 > 0):
            up = self.l[row - 2][col - 1]
        if(row < self.s):
            down = self.l[row][col - 1]
        return (up, down)

    def adjacent_horizontal_numbers(self, row: int, col: int):
        """Devolve os valores imediatamente à esquerda e à direita,
        respectivamente."""
        left = None
        right = None
        if(col - 1 > 0):
            left = self.l[row - 1][col - 2]
        if(col < self.s):
            right = self.l[row - 1][col]
        return (left, right)

    @staticmethod
    def parse_instance_from_stdin():
        """Lê o test do standard input (stdin) que é passado como argumento
        e retorna uma instância da classe Board.

        Por exemplo:
            $ python3 takuzu.py < input_T01

            > from sys import stdin
            > stdin.readline()
        """
        from sys import stdin
        return Board(stdin.read())

    # Outros metodos da classe
    def lyt(self):
        return self.l

    def size(self) -> int:
        return self.s

    def setPiece(self, row, col, val):
        self.l[row - 1][col - 1] = val

    def toString (self):
        s = ''
        for row in self.l:
            for val in row:
                s += str(val) + '\t'
            s += '\n'
        return s
    

class Takuzu(Problem):
    def __init__(self, board: Board):
        """O construtor especifica o estado inicial."""
        # TODO
        pass

    def actions(self, state: TakuzuState):
        """Retorna uma lista de ações que podem ser executadas a
        partir do estado passado como argumento."""
        # TODO
        pass

    def result(self, state: TakuzuState, action):
        """Retorna o estado resultante de executar a 'action' sobre
        'state' passado como argumento. A ação a executar deve ser uma
        das presentes na lista obtida pela execução de
        self.actions(state)."""
        # TODO
        pass

    def goal_test(self, state: TakuzuState):
        """Retorna True se e só se o estado passado como argumento é
        um estado objetivo. Deve verificar se todas as posições do tabuleiro
        estão preenchidas com uma sequência de números adjacentes."""
        # TODO
        pass

    def h(self, node: Node):
        """Função heuristica utilizada para a procura A*."""
        # TODO
        pass

    # TODO: outros metodos da classe


if __name__ == "__main__":

    b = Board.parse_instance_from_stdin()
    print(b.lyt())
    print(b.adjacent_vertical_numbers(1,4))
    print(b.adjacent_horizontal_numbers(1,4))

    
    # TODO:
    # Ler o ficheiro do standard input,
    # Usar uma técnica de procura para resolver a instância,
    # Retirar a solução a partir do nó resultante,
    # Imprimir para o standard output no formato indicado.
