'''
In a N x N grid representing a field of cherries, each cell is one of three possible integers.

 

0 means the cell is empty, so you can pass through;
1 means the cell contains a cherry, that you can pick up and pass through;
-1 means the cell contains a thorn that blocks your way.
 

Your task is to collect maximum number of cherries possible by following the rules below:

 

Starting at the position (0, 0) and reaching (N-1, N-1) by moving right or down through valid path cells (cells with value 0 or 1);
After reaching (N-1, N-1), returning to (0, 0) by moving left or up through valid path cells;
When passing through a path cell containing a cherry, you pick it up and the cell becomes an empty cell (0);
If there is no valid path between (0, 0) and (N-1, N-1), then no cherries can be collected.
 

 

Example 1:

Input: grid =
[[0, 1, -1],
 [1, 0, -1],
 [1, 1,  1]]
Output: 5
Explanation: 
The player started at (0, 0) and went down, down, right right to reach (2, 2).
4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
Then, the player went left, up, up, left to return home, picking up one more cherry.
The total number of cherries picked up is 5, and this is the maximum possible.
 

Note:

grid is an N by N 2D array, with 1 <= N <= 50.
Each grid[i][j] is an integer in the set {-1, 0, 1}.
It is guaranteed that grid[0][0] and grid[N-1][N-1] are not -1.
'''

class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        f = [[[float('-inf') for i in xrange(len(grid))] for i in xrange(len(grid))] for k in xrange(len(grid) + len(grid[0]) - 1)]
        if grid[0][0] >= 0:
            f[0][0][0] = grid[0][0]
        
        for k in xrange(1, len(grid) + len(grid[0]) - 1):
            for rowa in xrange(len(grid)):
                cola = k - rowa
                if cola < 0 or len(grid[0]) <= cola or grid[rowa][cola] == -1:
                    continue
                for rowb in xrange(rowa, len(grid)):
                    colb = k - rowb
                    if colb < 0 or len(grid[0]) <= colb or grid[rowb][colb] == -1:
                        continue
                        
                    
                    if 0 <= rowa - 1 and grid[rowa-1][cola] != -1 and grid[rowb-1][colb] != -1:
                        f[k][rowa][rowb] = max(f[k][rowa][rowb], f[k-1][rowa-1][rowb-1])
                    if 0 <= colb - 1 and grid[rowb][colb-1] != -1 and grid[rowa][cola-1] != -1:
                        f[k][rowa][rowb] = max(f[k][rowa][rowb], f[k-1][rowa][rowb])
                    if 0 <= rowa - 1 and grid[rowa-1][cola] != -1 and 0 <= colb - 1 and grid[rowb][colb-1] != -1:
                        f[k][rowa][rowb] = max(f[k][rowa][rowb], f[k-1][rowa-1][rowb])
                    if rowa != rowb:
                        f[k][rowa][rowb] = max(f[k][rowa][rowb], f[k-1][rowa][rowb-1])
                        
                    if rowa == rowb:
                        f[k][rowa][rowb] += grid[rowa][cola]
                    else:
                        f[k][rowa][rowb] += grid[rowa][cola] + grid[rowb][colb]
                        
        return max(0, f[len(grid) + len(grid[0])-2][len(grid)-1][len(grid)-1])
                        
                    
