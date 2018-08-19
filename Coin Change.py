'''
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1

Note:
You may assume that you have an infinite number of each kind of coin.

'''

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        dic = {0: 0}
        
        res = self.find(coins, dic, amount)
        if res == float('inf'):
            return -1
        return res
    
    def find(self, coins, dic, amount):
        if amount in dic:
            return dic[amount]
        res = float('inf')
        for c in coins:
            if amount >= c:
                res = min(res, self.find(coins, dic, amount - c) + 1)
        
        dic[amount] = res
        return dic[amount]
