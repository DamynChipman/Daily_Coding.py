"""
This problem was asked by Dropbox.

Conway's Game of Life takes place on an infinite two-dimensional board of square cells. Each cell is either dead or alive, and at each tick, the following rules apply:

Any live cell with less than two live neighbours dies.
Any live cell with two or three live neighbours remains living.
Any live cell with more than three live neighbours dies.
Any dead cell with exactly three live neighbours becomes a live cell.
A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.

Implement Conway's Game of Life. It should be able to be initialized with a starting list of live cell coordinates and the number of steps it should run for. Once initialized, it should print out the board state at each step. Since it's an infinite board, print out only the relevant coordinates, i.e. from the top-leftmost live cell to bottom-rightmost live cell.

You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).
"""

# ===== Solution =====
class GameOfLife:

    board = []
    NSTEPS = 0

    def __init__(self, start_live_cells, N):
        self.NSTEPS = N

        return None

    def __checkNeighbors(self, pos):
        row = pos[0]
        col = pos[1]
        to_return = 0

        if board[row+1, col] == '*':
            to_return += 1
        if board[row-1, col] == '*':
            to_return += 1
        if board[row, col+1] == '*':
            to_return += 1
        if board[row, col-1] == '*':
            to_return += 1
        if board[row+1, col+1] == '*':
            to_return += 1
        if board[row-1, col+1] == '*':
            to_return += 1
        if board[row+1, col-1] == '*':
            to_return += 1
        if board[row-1, col-1] == '*':
            to_return += 1

        return to_return

    def __tick(self):
        new_board = self.board
        
