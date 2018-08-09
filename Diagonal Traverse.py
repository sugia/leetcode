'''
 Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output:  [1,2,4,7,5,3,6,8,9]
Explanation:

Note:

    The total number of elements of the given matrix will not exceed 10,000.

'''

class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if not matrix or not matrix[0]:
            return res
        
        m = len(matrix)
        n = len(matrix[0])
        
        '''
        for step in xrange(m + n - 1):
            if step & 1:
                # goes down left
                for i in xrange(max(step + 1 - n, 0), min(step + 1, m)):
                    if 0 <= step - i < n:
                        res.append(matrix[i][step - i])
            else:
                # goes up right
                for i in reversed(xrange(max(step + 1 - n, 0), min(step + 1, m))):
                    if 0 <= step - i < n:
                        res.append(matrix[i][step - i])
        '''
        i, j = 0, 0
        up = True
        for step in xrange(m * n):
            res.append(matrix[i][j])
            if up:
                if 0 <= i - 1 < m and 0 <= j + 1 < n:
                    i -= 1
                    j += 1
                else:
                    if 0 <= j + 1 < n:
                        j += 1
                        up = False
                    else:
                        i += 1
                        up = False
            else:
                if 0 <= i + 1 < m and 0 <= j - 1 < n:
                    i += 1
                    j -= 1
                else:
                    if 0 <= i + 1 < m:
                        i += 1
                        up = True
                    else:
                        j += 1
                        up = True
        return res
