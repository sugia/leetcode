'''
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.

Follow up: 
Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
'''

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        n = len(board)
        m = len(board[0])
        
        copy_board = [[board[i][j] for j in xrange(m)] for i in xrange(n)]
        for i in xrange(n):
            for j in xrange(m):
                live_neighbors = 0
                for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    ii = i + x
                    jj = j + y
                    if 0 <= ii < n and 0 <= jj < m:
                        if copy_board[ii][jj] == 1:
                            live_neighbors += 1
                    
                if copy_board[i][j] == 1:
                    if live_neighbors < 2:
                        board[i][j] = 0
                    elif live_neighbors < 4:
                        board[i][j] = 1
                    else:
                        board[i][j] = 0
                elif copy_board[i][j] == 0:
                    if live_neighbors == 3:
                        board[i][j] = 1
                    else:
                        board[i][j] = 0
        
