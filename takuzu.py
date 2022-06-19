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

class Board:
    def __init__(self, n, board, free) -> None:
        """Representação interna de um tabuleiro de Takuzu."""
        self.s = n
        self.l = board
        self.f = free

    def get_number(self, row: int, col: int) -> int:
        """Devolve o valor na respetiva posição do tabuleiro."""
        return self.l[row][col]

    def adjacent_vertical_numbers(self, row: int, col: int):
        """Devolve os valores imediatamente abaixo e acima,
        respectivamente."""
        up = None
        down = None
        if(row > 0):
            up = self.l[row - 1][col]
        if(row < self.s - 1):
            down = self.l[row + 1][col]
        return (down, up)

    def adjacent_horizontal_numbers(self, row: int, col: int):
        """Devolve os valores imediatamente à esquerda e à direita,
        respectivamente."""
        left = None
        right = None
        if(col > 0):
            left = self.l[row][col - 1]
        if(col < self.s - 1):
            right = self.l[row][col + 1]
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
        free = 0
        n = int(input[0])
        input = input[1:(n + 1)]
        
        for i in range(n):
            input[i] = input[i].split('\t')
            input[i] = [int(x) for x in input[i]]
            for y in input[i]:
                if y == 2:
                    free += 1

        return Board(n, input, free)

    # Outros metodos da classe
    def set_number(self, row, col, val):
        self.l[row][col] = val
        self.f -= 1

    def transpose(self):
        n = self.s
        board = []
        for i in range(n):
            col = []
            for row in self.l:
                col.append(row[i])
            board.append(col)
        return board

    def chk_values(self):
        n = self.s
        b = self.l
        t = self.transpose()
        for i in range(n):
            if (chk_line(n, b[i]) == False) or (chk_line(n, t[i]) == False):
                return False
            for j in range(n-i): 
                if ((b[j+i] == b[i]) or (t[j+i] == t[i])) and (j+i) != i:
                    return False
        return True

    def copy(self):
        board = []

        for row in self.l:
            board.append(row[:])

        return Board(self.s, board, self.f)

    def toString (self):
        s = ''
        for row in self.l:
            for i in range(self.s):
                s += str(row[i])
                if i == self.s-1:
                    s += '\n'
                else:
                    s += '\t'
        return s
    
    def __str__(self):
        return self.toString()

class Takuzu(Problem):
    def __init__(self, board: Board):
        """O construtor especifica o estado inicial."""
        self.initial = TakuzuState(board)

    def actions(self, state: TakuzuState):
        """Retorna uma lista de ações que podem ser executadas a
        partir do estado passado como argumento."""
        b = state.board
        n = b.s
        actions = []
        for row in range(n):
            for col in range(n):
                if b.get_number(row, col) == 2:
                    actions.append((row, col, 0))
                    actions.append((row, col, 1))
        return actions

    def result(self, state: TakuzuState, action):
        """Retorna o estado resultante de executar a 'action' sobre
        'state' passado como argumento. A ação a executar deve ser uma
        das presentes na lista obtida pela execução de
        self.actions(state)."""
        board = state.board.copy()
        board.set_number(action[0], action[1], action[2])
        return TakuzuState(board)

    def goal_test(self, state: TakuzuState):
        """Retorna True se e só se o estado passado como argumento é
        um estado objetivo. Deve verificar se todas as posições do tabuleiro
        estão preenchidas com uma sequência de números adjacentes."""
        return ((state.board.f == 0) and (state.board.chk_values()))

    def h(self, node: Node):
        """Função heuristica utilizada para a procura A*."""
        # TODO
        pass

    # TODO: outros metodos da classe


def chk_line(n, line):
    max = abs(-n//2)
    count_0, count_1, seq_0, seq_1 = 0, 0, 0, 0
    for x in line:
        if x == 0:
            count_0 += 1
            seq_0 += 1
            seq_1 = 0
        elif x == 1:
            count_1 += 1
            seq_0 = 0
            seq_1 += 1
        if (count_0 > max) or (count_1 > max) or (seq_1 > 2) or (seq_0 > 2):
                return False
    return True


if __name__ == "__main__":

    board = Board.parse_instance_from_stdin()
    # Criar uma instância de Takuzu:
    problem = Takuzu(board)
    # Obter o nó solução usando a procura em profundidade:
    goal_node = depth_first_tree_search(problem)
    print(goal_node.state.board, end="")

    # TODO:
    # Ler o ficheiro do standard input,
    # Usar uma técnica de procura para resolver a instância,
    # Retirar a solução a partir do nó resultante,
    # Imprimir para o standard output no formato indicado.
