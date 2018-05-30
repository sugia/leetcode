'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if not matrix:
            return res 
        upper_bound = 0
        lower_bound = len(matrix) - 1
        left_bound = 0
        right_bound = len(matrix[0]) - 1
        
        i = 0
        j = 0
        while upper_bound <= i <= lower_bound and left_bound <= j <= right_bound:
            # go right
            res.append(matrix[i][j])

            while j + 1 <= right_bound:
                j = j + 1
                res.append(matrix[i][j])
            # go down
            if i + 1 > lower_bound:
                break
            while i + 1 <= lower_bound:
                i = i + 1
                res.append(matrix[i][j])
            # go left
            if left_bound > j - 1:
                break
            while left_bound <= j - 1:
                j = j - 1
                res.append(matrix[i][j])
            # go up

            while upper_bound < i - 1:
                i = i - 1
                res.append(matrix[i][j])
            upper_bound += 1
            lower_bound -= 1
            left_bound += 1
            right_bound -= 1
            j = j + 1
        
        return res
