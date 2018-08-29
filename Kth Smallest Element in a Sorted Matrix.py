'''
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.

Note:
You may assume k is always valid, 1 ≤ k ≤ n2.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        visited = [[False for j in xrange(len(matrix[0]))] for i in xrange(len(matrix))]
        h = []
        heapq.heappush(h, (matrix[0][0], 0, 0))
        visited[0][0] = True
        for _ in xrange(k):
            val, x, y = heapq.heappop(h)
            if _ == k-1:
                return val
            if x+1 < len(matrix) and not visited[x+1][y]:
                visited[x+1][y] = True
                heapq.heappush(h, (matrix[x+1][y], x+1, y))
            if y+1 < len(matrix[0]) and not visited[x][y+1]:
                visited[x][y+1] = True
                heapq.heappush(h, (matrix[x][y+1], x, y+1))
        return -1
