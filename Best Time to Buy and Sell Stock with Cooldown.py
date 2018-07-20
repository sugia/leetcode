'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

    You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
    After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

Example:

Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]


'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        
        
        # hold + do nothing = hold
        # hold + sell = cooldown
        # not hold + do nothing = not hold
        # not hold + buy = hold
        # cooldown + do nothing = not hold
        
        # not hold <= not hold + do nothing, cooldown + do nothing
        # hold <= hold + do nothing, not hold + buy
        # cooldown <= hold + sell
        
        hold, not_hold, cooldown = float('-inf'), 0, float('-inf')
        
        for x in prices:
            hold, not_hold, cooldown = max(hold, not_hold - x), max(not_hold, cooldown), hold + x
            
        return max(hold, not_hold, cooldown)
