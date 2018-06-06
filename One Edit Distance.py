'''
Given two strings s and t, determine if they are both one edit distance apart.

Note: 

There are 3 possiblities to satisify one edit distance apart:

Insert a character into s to get t
Delete a character from s to get t
Replace a character of s to get t
Example 1:

Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.
Example 2:

Input: s = "cab", t = "ad"
Output: false
Explanation: We cannot get t from s by only one step.
Example 3:

Input: s = "1203", t = "1213"
Output: true
Explanation: We can replace '0' with '1' to get t.
'''

class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return len(t) == 1
        if len(t) == 0:
            return len(s) == 1
        
        if abs(len(s) - len(t)) > 1:
            return False
        
        if len(s) > len(t):
            return self.isOneEditDistance(t, s)
        
        left = -1
        while left < len(s) - 1 and s[left + 1] == t[left + 1]:
            left += 1
            
        if left == len(s) - 1 and len(s) + 1 == len(t):
            return True
        
        right = len(s)
        right_t = len(t)
        while right > 0 and s[right - 1] == t[right_t - 1]:
            right -= 1
            right_t -= 1
            
        if left + 1 == right:
            return True
        
        if left + 2 == right and len(s) == len(t):
            return True
        
        return False
