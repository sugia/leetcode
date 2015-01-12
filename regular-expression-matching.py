class Solution:
    #given two strings
    #return a bool
    def isMatch(self, s, p):
        dp = [[False for j in range(len(p)+1)] for i in range(len(s)+1)]
        dp[0][0] = True
        for j in range(2, len(p)+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-2] or dp[i][j-1] or (dp[i-1][j] and (p[j-2] == '.' or s[i-1] == p[j-2]))
                else:
                    dp[i][j] = dp[i-1][j-1] and s[i-1] == p[j-1]
        return dp[-1][-1]
