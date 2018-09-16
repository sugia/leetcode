'''
Given an integer n, find the closest integer (not including itself), which is a palindrome.

The 'closest' is defined as absolute difference minimized between two integers.

Example 1:
Input: "123"
Output: "121"
Note:
The input n is a positive integer represented by string, whose length will not exceed 18.
If there is a tie, return the smaller one as answer.
'''

class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        mid = len(n) // 2
        if len(n) & 1:
            res = n[:mid+1] + n[:mid][::-1]
        else:
            res = n[:mid] + n[:mid][::-1]
        for i in xrange(10):
            if len(n) & 1:
                tmp = res[:mid] + str(i) + res[mid+1:]
            else:
                tmp = res[:mid-1] + str(i) + str(i) + res[mid+1:]
                
            if res == n:
                res = tmp
            elif tmp == n:
                continue
            elif self.diff(tmp, n) < self.diff(res, n):
                res = tmp
            elif self.diff(tmp, n) == self.diff(res, n) and int(tmp) < int(res):
                res = tmp

        if len(n) > 1:
            tmp = '9' * (len(n) - 1)
            if self.diff(tmp, n) <= self.diff(res, n):
                res = tmp
        tmp = '1' + '0' * (len(n) - 1) + '1'
        if self.diff(tmp, n) < self.diff(res, n):
            res = tmp
        
        return res
        
    def diff(self, x, y):
        return abs(int(x) - int(y))
        
