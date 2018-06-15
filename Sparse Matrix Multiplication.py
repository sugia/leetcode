'''
Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

Input:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

Output:

     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |


'''

class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        row_a = len(A)
        col_a = len(A[0])
        
        row_b = len(B)
        col_b = len(B[0])
        
        res = [[0 for j in xrange(col_b)] for i in xrange(row_a)]
        
        ka = {}
        kb = {}
        
        for i in xrange(row_a):
            for j in xrange(col_a):
                if A[i][j] != 0:
                    if j not in ka:
                        ka[j] = [(i, A[i][j])]
                    else:
                        ka[j].append((i, A[i][j]))
                        
        for i in xrange(row_b):
            for j in xrange(col_b):
                if B[i][j] != 0:
                    if i not in kb:
                        kb[i] = [(j, B[i][j])]
                    else:
                        kb[i].append((j, B[i][j]))
        
        for k in ka:
            if k in kb:
                for (row, val_a) in ka[k]:
                    for (col, val_b) in kb[k]:
                        res[row][col] += val_a * val_b
                
        return res
