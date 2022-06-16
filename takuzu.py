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
    def __init__(self, n, board) -> None:
        """Representação interna de um tabuleiro de Takuzu."""
        self.s = n
        self.l = board

    def get_number(self, row: int, col: int) -> int:
        """Devolve o valor na respetiva posição do tabuleiro."""
        return self.l[row - 1][col - 1]

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
        input = stdin.read()
        input = input.split('\n')
        n = int(input[0])
        input = input[1:(n + 1)]

        for i in range(n):
            input[i] = input[i].split('\t')
            input[i] = [int(x) for x in input[i]]

        return Board(n, input)

    # Outros metodos da classe
    def lyt(self):
        return self.l

    def size(self) -> int:
        return self.s

    def set_number(self, row, col, val):
        self.l[row - 1][col - 1] = val

    def get_col(self, n):
        col = []
        for row in self.l:
            col.append(row(n - 1))
        return col

    def get_row(self, n):
        return self.l[n - 1]

    def copy(self):
        board = []

        for row in self.l:
            board.append(row[:])

        return Board(self.s, board)

    def toString (self):
        s = ''
        for row in self.l:
            for val in row:
                s += str(val) + '\t'
            s += '\n'
        return s
    
    def __str__(self):
        return self.toString()

class Takuzu(Problem):
    def __init__(self, board: Board):
        """O construtor especifica o estado inicial."""
        self = board

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
        board = state.bd().copy()
        board.set_number(action[0], action[1], action[2])
        return TakuzuState(board)

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

    board = Board.parse_instance_from_stdin()
    print("Initial:\n", board, sep="")
    # Criar uma instância de Takuzu:
    problem = Takuzu(board)
    # Criar um estado com a configuração inicial:
    initial_state = TakuzuState(board)
    # Mostrar valor na posição (2, 2):
    print(initial_state.board.get_number(2, 2))
    # Realizar acção de inserir o número 1 na posição linha 2 e coluna 2
    result_state = problem.result(initial_state, (2, 2, 1))
    # Mostrar valor na posição (2, 2):
    print(result_state.board)
    print(result_state.board.get_number(2, 2))
    

    # TODO:
    # Ler o ficheiro do standard input,
    # Usar uma técnica de procura para resolver a instância,
    # Retirar a solução a partir do nó resultante,
    # Imprimir para o standard output no formato indicado.
