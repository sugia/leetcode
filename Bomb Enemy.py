'''

Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
Note: You can only put the bomb at an empty cell.

Example:

Input: [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
Output: 3 
Explanation: For the given grid,

0 E 0 0 
E 0 W E 
0 E 0 0

Placing a bomb at (1,1) kills 3 enemies.
'''

class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        res = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[i])):
                if grid[i][j] == '0':
                    res = max(res, self.find(grid, i, j))
        return res
    
    def find(self, grid, x, y):
        res = 0
        i = x + 1
        while i < len(grid) and grid[i][y] != 'W':
            if grid[i][y] == 'E':
                res += 1
            i += 1
        i = x - 1
        while 0 <= i and grid[i][y] != 'W':
            if grid[i][y] == 'E':
                res += 1
            i -= 1
            
        j = y + 1
        while j < len(grid[0]) and grid[x][j] != 'W':
            if grid[x][j] == 'E':
                res += 1
            j += 1
        j = y - 1
        while 0 <= j and grid[x][j] != 'W':
            if grid[x][j] == 'E':
                res += 1
            j -= 1
        return res
