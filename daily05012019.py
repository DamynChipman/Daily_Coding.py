"""
This problem was asked by Microsoft.

You have an N by N board. Write a function that, given N, returns the number of possible arrangements of the board where N queens can be placed on the board without threatening each other, i.e. no two queens share the same row, column, or diagonal.
"""

# ===== Test Cases =====

# ===== Solution =====
import numpy as np

class Board:

    # === ATTRIBUTES ===
    squares = []
    size = 0

    # === METHODS ===
    def __init__(self, N):

        self.squares = np.zeros((N,N), dtype = int)
        self.size = N

        return None


    def placeQueen(self, pos):

        row = pos[0]
        col = pos[1]

        if row > self.size or col > self.size:
            return False

        if self._isValid(pos):
            # go through cols
            for j in np.arange(0,self.size):
                self.squares[row, j] = 1

            # go through rows
            for i in np.arange(0,self.size):
                self.squares[i, col] = 1

            # go through diag


            self.squares[row, col] = 2
            return True
        else:
            return False


    def numbQueens(self):
        NQueens = 0
        for row in self.squares:
            for square in row:
                if square == 2:
                    NQueens += 1
        return NQueens


    def toString(self):

        to_return = ''
        for row in self.squares:
            for square in row:
                to_return += str(square)
                to_return += '  '
            to_return += '\n'

        return to_return


    def _isValid(self, pos):

        row = pos[0]
        col = pos[1]

        if self.squares[row, col] == 1 or self.squares[row, col] == 2:
            return False

        return True

def findArrangements(N):
    boards = []
    for i in np.arange(0, N):
        for j in np.arange(0, N):
            board = Board(N)
            if board.placeQueen([i,j]):
                boards.append(board)

    

    for board in boards:
        print(board.toString())
    return len(boards)


# ===== Debugging =====
Ns = [0,1,2,3,4,5,6,7,8,9,10]
board = Board(8)
board.placeQueen([2,4])
board.placeQueen([5,2])
board.placeQueen([0,0])
print(board.toString())
print(board.numbQueens())

print('TESTING:')
print(findArrangements(3))
