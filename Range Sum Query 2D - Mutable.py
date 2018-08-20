'''
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:

Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
update(3, 2, 2)
sumRegion(2, 1, 4, 3) -> 10

Note:

    The matrix is only modifiable by the update function.
    You may assume the number of calls to update and sumRegion function is distributed evenly.
    You may assume that row1 ≤ row2 and col1 ≤ col2.

'''

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        
        self.org = []
        for i in xrange(len(matrix)):
            self.org.append([])
            for j in xrange(len(matrix[i])):
                self.org[-1].append(matrix[i][j])
                
        self.sum = []
        for i in xrange(len(matrix)):
            self.sum.append([])
            for j in xrange(len(matrix[i])):
                self.sum[-1].append(matrix[i][j])
                
        for i in xrange(len(self.sum)):
            for j in xrange(len(self.sum[i])):
                if j == 0:
                    self.sum[i][j] = self.org[i][j]
                else:
                    self.sum[i][j] = self.sum[i][j-1] + self.org[i][j]
        
    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        self.org[row][col] = val
        
        for j in xrange(col, len(self.sum[row])):
            if j == 0:
                self.sum[row][j] = self.org[row][j]
            else:
                self.sum[row][j] = self.sum[row][j-1] + self.org[row][j]
     
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        res = 0
        for row in xrange(row1, row2+1):
            if col1 == 0:
                res += self.sum[row][col2]
            else:
                res += self.sum[row][col2] - self.sum[row][col1-1]
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
