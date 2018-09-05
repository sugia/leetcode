'''
Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

Example 1:

Input: a = 2, b = [3]
Output: 8
Example 2:

Input: a = 2, b = [1,0]
Output: 1024
'''

class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        y = 0
        for x in b:
            y = y * 10 + x
        return self.get(a, y)
    
    def get(self, a, b):
        if b == 0:
            return 1
        elif b == 1:
            return a % 1337
        else:
            if b & 1:
                return self.get(a, b // 2) ** 2 * a % 1337
            else:
                return self.get(a, b // 2) ** 2 % 1337
