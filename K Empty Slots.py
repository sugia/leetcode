'''
There is a garden with N slots. In each slot, there is a flower. The N flowers will bloom one by one in N days. In each day, there will be exactly one flower blooming and it will be in the status of blooming since then.

Given an array flowers consists of number from 1 to N. Each number in the array represents the place where the flower will open in that day.

For example, flowers[i] = x means that the unique flower that blooms at day i will be at position x, where i and x will be in the range from 1 to N.

Also given an integer k, you need to output in which day there exists two flowers in the status of blooming, and also the number of flowers between them is k and these flowers are not blooming.

If there isn't such day, output -1.

Example 1:
Input: 
flowers: [1,3,2]
k: 1
Output: 2
Explanation: In the second day, the first and the third flower have become blooming.
Example 2:
Input: 
flowers: [1,2,3]
k: 1
Output: -1
Note:
The given array will be in the range [1, 20000].
'''

class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        vec = [0 for i in xrange(len(flowers)+1)]
        
        box = set()
        for i in xrange(len(flowers)):
            idx = flowers[i]
            self.add(vec, idx, 1)
            if idx-k-1 in box:
                if self.get(vec, idx) - self.get(vec, idx-k-1) == 1:
                    return i+1
            if idx+k+1 in box:
                if self.get(vec, idx+k+1) - self.get(vec, idx) == 1:
                    return i+1
            box.add(idx)
        return -1
    
    def add(self, vec, idx, val):
        while idx < len(vec):
            vec[idx] += val
            idx += (idx & -idx)
    
    def get(self, vec, idx):
        res = 0
        while idx > 0:
            res += vec[idx]
            idx -= (idx & - idx)
        return res
    
