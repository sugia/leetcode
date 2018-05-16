'''

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        fre = {}
        for c in s:
            if c in fre:
                fre[c] += 1
            else:
                fre[c] = 1
                
        res = 0
        has_odd = False
        for c in fre:
            if fre[c] % 2 == 0:
                res += fre[c]
            else:
                has_odd = True
                res += fre[c] - 1
                
        if has_odd:
            res += 1
        return res
