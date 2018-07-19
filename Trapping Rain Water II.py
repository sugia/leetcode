'''
Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map, compute the volume of water it is able to trap after raining.

Note:
Both m and n are less than 110. The height of each unit cell is greater than 0 and is less than 20,000.

Example:

Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.


The above image represents the elevation map [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] before the rain.


After the rain, water is trapped between the blocks. The total volume of water trapped is 4. 
'''

import heapq

class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        
        if not heightMap:
            return 0
        heap = []
        m = len(heightMap)
        n = len(heightMap[0])
        
        visited = [[False for j in xrange(n)] for i in xrange(m)]
        for i in xrange(m):
            if not visited[i][0]:
                visited[i][0] = True
                heapq.heappush(heap, (heightMap[i][0], i, 0))
            if not visited[i][n-1]:
                visited[i][n-1] = True
                heapq.heappush(heap, (heightMap[i][n-1], i, n-1))
                
        for j in xrange(n):
            if not visited[0][j]:
                visited[0][j] = True
                heapq.heappush(heap, (heightMap[0][j], 0, j))
            if not visited[m-1][j]:
                visited[m-1][j] = True
                heapq.heappush(heap, (heightMap[m-1][j], m-1, j))
                
        tmp = 0
        res = 0
        while heap:
            h, x, y = heapq.heappop(heap)
            tmp = max(tmp, h)
            for (i, j) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if 0 <= x + i < m and 0 <= y + j < n:
                    if not visited[x+i][y+j]:
                        visited[x+i][y+j] = True
                        if heightMap[x+i][y+j] < tmp:
                            res += tmp - heightMap[x+i][y+j]
                        heapq.heappush(heap, (heightMap[x+i][y+j], x+i, y+j))
                        
        return res
