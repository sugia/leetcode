'''

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        if not grid:
            return res
            
        for i in xrange(len(grid)):
            for j in xrange(len(grid[i])):
                if grid[i][j] == '1':
                    res += 1
                    self.fill(grid, i, j)
                    
        return res
    
    def fill(self, grid, x, y):
        vec = [(x, y)]
        while len(vec) > 0:
            tmpx, tmpy = vec.pop()
            grid[tmpx][tmpy] = '0'
            for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                tmpxx = tmpx + i
                tmpyy = tmpy + j
                if 0 <= tmpxx < len(grid) and 0 <= tmpyy < len(grid[tmpxx]):
                    if grid[tmpxx][tmpyy] == '1':
                        vec.append((tmpxx, tmpyy))
                    
