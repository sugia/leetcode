'''
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
'''

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        res = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[i])):
                if grid[i][j] == 1:
                    res = max(res, self.find(grid, i, j))
                    
        return res 
    
    def find(self, grid, x, y):
        res = 1
        vec = [(x, y)]
        grid[x][y] = 0
        while vec:
            next_vec = []
            for pair in vec:
                for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_x, new_y = pair[0] + i, pair[1] + j
                    if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[new_x]):
                        if grid[new_x][new_y] == 1:
                            res += 1
                            next_vec.append((new_x, new_y))
                            grid[new_x][new_y] = 0
                            
            vec = next_vec
                            
        return res
                            
