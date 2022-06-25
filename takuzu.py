# takuzu.py: Template para implementação do projeto de Inteligência Artificial 2021/2022.
# Devem alterar as classes e funções neste ficheiro de acordo com as instruções do enunciado.
# Além das funções e classes já definidas, podem acrescentar outras que considerem pertinentes.

# Grupo 00:
# 00000 Nome1
# 00000 Nome2

import sys
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
    def __init__(self, n, board) -> None:
        """Representação interna de um tabuleiro de Takuzu."""
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
        n = int(input[0])
        input = input[1:(n + 1)]
        
        for i in range(n):
            input[i] = input[i].split('\t')
            input[i] = [int(x) for x in input[i]]

        return Board(n, input)

    # Outros metodos da classe
    def set_number(self, row, col, val):
        self.l[row][col] = val

    def get_column(self, n):
        col = []
        for row in self.l:
            col.append(row[n])
        return col

    def copy(self):
        board = []

        for row in self.l:
            board.append(row[:])

        return Board(self.s, board)

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
        s = ''
        for row in self.l:
            for i in range(self.s):
                s += str(row[i])
                if i == self.s-1:
                    s += '\n'
                else:
                    s += '\t'
        return s

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
                    if chk_pos(b, row, col, 0):
                        actions.append((row, col, 0))
                    if chk_pos(b, row, col, 1):
                        actions.append((row, col, 1))
                    return actions

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
        n = state.board.s
        b = state.board.l
        t = [list(i) for i in zip(*b)]

        for line in b:
            if line.count(2) != 0:
                return False
        
        for j in range(n):
            if chk_line(b[j]):
                return False 
            if chk_line(t[j]):
                return False
            if abs(b[j].count(0) - b[j].count(1)) > 1:
                return False
            if (t[j].count(0) - t[j].count(1)) > 1:
                return False

        for row in b:
            if b.count(row) > 1:
                return False
        for col in t:
            if t.count(col) > 1:
                return False
        
        return True

    def h(self, node: Node):
        """Função heuristica utilizada para a procura A*."""
        # TODO
        pass

    # TODO: outros metodos da classe

def chk_line(line):
    c0, c1 = 0, 0
    for x in line:
        if x == 0:
            c0 += 1
            c1 = 0
        elif x == 1:
            c0 = 0
            c1 += 1
        elif x == 2:
            c0 = 0
            c1 = 0
        if c0 > 2 or c1 > 2:
            return True
    return False

def chk_pos(board, row, col, val):
    n = board.s
    max = abs(-n//2)

    r = board.l[row][:]
    r[col] = val
    c = board.get_column(col)
    c[row] = val

    if chk_line(r) or (r.count(val) > max):
        return False
    if chk_line(c) or (c.count(val) > max):
        return False
    
    return True



if __name__ == "__main__":

    board = Board.parse_instance_from_stdin()
    problem = Takuzu(board)

    # search algorithm
    goal_node = depth_first_tree_search(problem)

    print(goal_node.state.board, sep="", end="")
    
    # TODO:
    # Ler o ficheiro do standard input,
    # Usar uma técnica de procura para resolver a instância,
    # Retirar a solução a partir do nó resultante,
    # Imprimir para o standard output no formato indicado.
