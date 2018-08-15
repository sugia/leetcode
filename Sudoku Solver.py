'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

    Each of the digits 1-9 must occur exactly once in each row.
    Each of the digits 1-9 must occur exactly once in each column.
    Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

Empty cells are indicated by the character '.'.


A sudoku puzzle...


...and its solution numbers marked in red.

Note:

    The given board contain only digits 1-9 and the character '.'.
    You may assume that the given Sudoku puzzle will have a single unique solution.
    The given board size is always 9x9.


'''

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        self.solve(board)
        
    def solve(self, board):
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] == '.':
                    for c in xrange(1, 10):
                        if self.valid(board, i, j, str(c)):
                            board[i][j] = str(c)
                            if self.solve(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True
    
    def valid(self, board, x, y, c):
        for i in xrange(9):
            if board[x][i] == c:
                return False
            if board[i][y] == c:
                return False
            if board[3 * (x / 3) + i / 3][3 * (y / 3) + i % 3] == c:
                return False
        return True
            
                            
        
