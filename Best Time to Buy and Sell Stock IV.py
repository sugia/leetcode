'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:

Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.


'''

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        
        if len(prices) < 2 or k == 0:
            return 0
        
        if k * 2 >= len(prices):
            res = 0
            for i in xrange(1, len(prices)):
                res += max(0, prices[i] - prices[i-1])
            return res
            
            
        buy = [float('-inf') for i in xrange(k)]
        sell = [0 for i in xrange(k)]
        
        for x in prices:
            buy[0] = max(buy[0], -x)
            sell[0] = max(sell[0], x + buy[0])
            
            for i in xrange(1, k):
                buy[i] = max(buy[i], sell[i-1] - x)
                sell[i] = max(sell[i], x + buy[i])
                
        return sell[-1]
