'''
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

'''

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = [0 for i in xrange(n+1)]
        f[0] = 1
        for tot in xrange(1, n+1):
            for left in xrange(tot):
                 f[tot] += f[left] * f[tot - 1 - left]
        return f[-1]
            
