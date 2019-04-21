'''
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".
'''

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        f = [[0 for j in range(len(s))] for i in range(len(s))]
        for i in range(len(s)):
            f[i][i] = 1
            
        for l in range(2, len(s)+1):
            for i in range(len(s)-l+1):
                j = i + l - 1
                
                if s[i] == s[j]:
                    f[i][j] = max(f[i][j], f[i+1][j-1] + 2)
                else:
                    f[i][j] = max(f[i+1][j], f[i][j-1])
            
        return f[0][-1]
