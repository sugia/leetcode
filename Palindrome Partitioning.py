'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
'''

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.find(s, [], res)
        return res
    
    def find(self, s, tmp, res):
        if not s:
            res.append(tmp)
            return
        for i in xrange(1, len(s)+1):
            if self.valid(s[:i]):
                self.find(s[i:], tmp + [s[:i]], res)
                
    def valid(self, s):
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
