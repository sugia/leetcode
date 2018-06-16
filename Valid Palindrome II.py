'''
 Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:

Input: "aba"
Output: True

Example 2:

Input: "abca"
Output: True
Explanation: You could delete the character 'c'.

Note:

    The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

'''

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vec = list(s)
        
        left = 0
        right = len(vec) - 1
        while left < right:
            if s[left] != s[right]:
                return self.valid(s[left:right]) or self.valid(s[left+1:right+1])
            left += 1
            right -= 1
            
        return True
    
    def valid(self, vec):
        n = len(vec)
        for i in xrange(n // 2):
            if vec[i] != vec[n-i-1]:
                return False
        return True
