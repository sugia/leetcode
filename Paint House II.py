'''
There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:

Input: [[1,5,3],[2,9,4]]
Output: 5
Explanation: Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5; 
             Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5. 

Follow up:
Could you solve it in O(nk) runtime?

'''

class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        
        dp = [[float('inf') for j in xrange(len(costs[i]))] for i in xrange(len(costs))]
        
        for j in xrange(len(costs[0])):
            dp[0][j] = costs[0][j]
            
        for i in xrange(1, len(costs)):
            for j in xrange(len(costs[i])):
                for k in xrange(len(costs[i-1])):
                    if j == k:
                        continue
                    dp[i][j] = min(dp[i][j], costs[i][j] + dp[i-1][k])
                    
        return min(dp[-1])
