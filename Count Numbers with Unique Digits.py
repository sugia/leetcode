'''
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:

Input: 2
Output: 91 
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, 
             excluding 11,22,33,44,55,66,77,88,99
'''

class Solution:
    def __init__(self):
        self.f = {0: 1, 1: 9, 2: 9 * 9}
        for i in range(3, 11):
            self.f[i] = self.f[i-1] * (11 - i)
            
        for i in range(1, 11):
            self.f[i] += self.f[i-1]
            
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n < 0:
            return 0
        if n > 10:
            return self.f[10]
        return self.f[n]
    
