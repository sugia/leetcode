'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:

The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.
'''

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.sum = [0 for i in xrange(len(nums)+1)]
        for i in xrange(len(nums)):
            self.add(i+1, nums[i])

    def add(self, idx, val):
        while idx < len(self.sum):
            self.sum[idx] += val
            idx += self.lowbit(idx)
            
    def lowbit(self, x):
        return x & -x
    
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.add(i+1, val - self.nums[i])
        self.nums[i] = val

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        
        return self.getsum(j+1) - self.getsum(i)
    
    def getsum(self, idx):
        res = 0
        while idx > 0:
            res += self.sum[idx]
            idx -= self.lowbit(idx)
        return res
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
