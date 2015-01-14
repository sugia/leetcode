class Solution:
    #given a list of integers
    #return an integer
    def trap(self, A):
        if len(A) == 0:
            return 0
        dp = []
        tmp = A[0]
        for i in range(len(A)):
            tmp = max(tmp, A[i])
            dp.append(tmp)
        res = 0
        tmp = A[-1]
        for i in range(len(A))[::-1]:
            tmp = max(tmp, A[i])
            res += min(dp[i], tmp) - A[i]
        return res
