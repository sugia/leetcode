'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:

Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
'''

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        f = [float('inf') for i in xrange(len(s))]
        for i in xrange(len(s)):
            if s[:i+1] == s[:i+1][::-1]:
                f[i] = 0
                
        pre = {}
        for i in xrange(len(s)):
            self.build(s, pre, i, i)
            self.build(s, pre, i, i+1)
        
        
        for i in xrange(len(s)):
            if i in pre:
                for j in pre[i]:
                    if 0 <= j-1:
                        f[i] = min(f[i], f[j-1] + 1)
        return f[-1]
    
    def build(self, s, pre, i, j):
        while 0 <= i and j < len(s):
            if s[i] == s[j]:
                if j in pre:
                    pre[j].append(i)
                else:
                    pre[j] = [i]
                i -= 1
                j += 1
            else:
                break
    
