'''
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
Example 1: 
Input:

0 0 0
0 1 0
0 0 0
Output:
0 0 0
0 1 0
0 0 0
Example 2: 
Input:

0 0 0
0 1 0
1 1 1
Output:
0 0 0
0 1 0
1 2 1
Note:
The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.
'''

class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return [[]]
        
        dis = [[float('inf') for j in xrange(len(matrix[i]))] for i in xrange(len(matrix))]
        
        vec = []
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[i])):
                if matrix[i][j] == 0:
                    dis[i][j] = 0
                    vec.append((i, j))
    
        while vec:
            next_vec = []
            for x, y in vec:
                for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    xx, yy = x+i, y+j
                    if 0 <= xx < len(matrix) and 0 <= yy < len(matrix[0]) and dis[xx][yy] > dis[x][y] + 1:
                        dis[xx][yy] = dis[x][y] + 1
                        next_vec.append((xx, yy))
            
            vec = next_vec
            
        return dis
