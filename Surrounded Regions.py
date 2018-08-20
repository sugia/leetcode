'''
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

'''

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return 
        
        visited = [[False for j in xrange(len(board[0]))] for i in xrange(len(board))]
        for i in xrange(len(board)):
            for j in xrange(len(board[i])):
                if board[i][j] == 'O' and not visited[i][j]:
                    self.fill(board, visited, i, j)
    
    def fill(self, board, visited, x, y):
        visited[x][y] = True
        vec = [(x, y)]
        is_boarder = False
        block = []
        while vec:
            a, b = vec.pop()
            block.append((a, b))
            if a == 0 or a == len(board) - 1 or b == 0 or b == len(board[0]) - 1:
                is_boarder = True
            
            for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                aa = a + i
                bb = b + j
                if 0 <= aa < len(board) and 0 <= bb < len(board[0]):
                    if board[aa][bb] == 'O' and not visited[aa][bb]:
                        visited[aa][bb] = True
                        vec.append((aa, bb))
        
        if not is_boarder:
            for a, b in block:
                board[a][b] = 'X'
                        
                
