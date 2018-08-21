'''
Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.

If there is no non-empty subarray with sum at least K, return -1.

 

Example 1:

Input: A = [1], K = 1
Output: 1

Example 2:

Input: A = [1,2], K = 4
Output: -1

Example 3:

Input: A = [2,-1,2], K = 3
Output: 3

 

Note:

    1 <= A.length <= 50000
    -10 ^ 5 <= A[i] <= 10 ^ 5
    1 <= K <= 10 ^ 9


'''

class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        s = [0]
        for x in A:
            s.append(s[-1] + x)
        res = float('inf')
        vec = []
        for i in xrange(len(s)):
            while vec and s[i] - s[vec[0]] >= K:
                res = min(res, i - vec[0])
                vec.pop(0)
            while vec and s[i] <= s[vec[-1]]:
                vec.pop()
            vec.append(i)
        
        if res == float('inf'):
            return -1
        else:
            return res
