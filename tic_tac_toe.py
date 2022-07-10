from typing import List

import numpy


class TicTacToe:
    def __init__(self, board: List):
        self.board = board

    def check_empty_board(self):
        board_items = [item for row in self.board for item in row]
        if all(board_item == ' ' for board_item in board_items):
            return True

    def find_winner(self, combination: List):
        if len(set(combination)) == 1:
            if combination[0] != ' ':
                return combination[0]
        return None

    def check_state(self):
        if self.check_empty_board():
            return 'The board is empty'
        rows = self.board
        columns = numpy.transpose(self.board).tolist()
        diags = [[rows[i][i] for i in range(len(rows))], [rows[i][~i] for i in range(len(rows))]]
        combinations = rows + columns + diags
        for combination in combinations:
            winner = self.find_winner(combination)
            if winner:
                return f'The winner is "{winner}"'
        return 'The game is on'


if __name__ == '__main__':
    boards = [
        [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ],
        [
            [' ', ' ', ' '],
            [' ', '0', ' '],
            [' ', ' ', ' ']
        ],
        [
            ['0', ' ', ' '],
            [' ', '0', ' '],
            [' ', ' ', '0']
        ],
        [
            ['X', 'X', 'X'],
            [' ', '0', ' '],
            [' ', ' ', ' ']
        ],
        [
            ['X', 'X', '0'],
            ['X', '0', ' '],
            ['X', ' ', ' ']
        ]
    ]
    for board in boards:
        print(*board, sep='\n')
        print(TicTacToe(board).check_state() + '\n')
