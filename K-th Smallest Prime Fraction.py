'''
A sorted list A contains 1, plus some number of primes.  Then, for every p < q in the list, we consider the fraction p/q.

What is the K-th smallest fraction considered?  Return your answer as an array of ints, where answer[0] = p and answer[1] = q.

Examples:
Input: A = [1, 2, 3, 5], K = 3
Output: [2, 5]
Explanation:
The fractions to be considered in sorted order are:
1/5, 1/3, 2/5, 1/2, 3/5, 2/3.
The third fraction is 2/5.

Input: A = [1, 7], K = 1
Output: [1, 7]
Note:

A will have length between 2 and 2000.
Each A[i] will be between 1 and 30000.
K will be between 1 and A.length * (A.length - 1) / 2.
'''

class Solution(object):
    def kthSmallestPrimeFraction(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        A.sort()
        h = []
        i = 0
        j = len(A)-1
        visited = set([(i, j)])
        heapq.heappush(h, (1.0 * A[i] / A[j], i, j))
        for idx in xrange(K):
            val, x, y = heapq.heappop(h)
            i = x
            j = y
            visited.remove((x, y))
            if (i+1, j) not in visited:
                visited.add((i+1, j))
                heapq.heappush(h, (1.0 * A[i+1] / A[j], i+1, j))
            if (i, j-1) not in visited:
                visited.add((i, j-1))
                heapq.heappush(h, (1.0 * A[i] / A[j-1], i, j-1))
            
        return [A[i], A[j]]
        
        
