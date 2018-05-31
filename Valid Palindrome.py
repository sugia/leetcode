'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
'''

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alpha = []
        for c in s:
            if c.isalnum():
                alpha.append(c.lower())
        
        for i in xrange(len(alpha) // 2):
            if alpha[i] != alpha[len(alpha) - i - 1]:
                return False
        return True
