'''
Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2

Example2:

Input: [2,4,3,5,1]
Output: 3

Note:

    The length of the given array will not exceed 50,000.
    All the numbers in the input array are in the range of 32-bit integer.

'''

class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.merge(nums, 0, len(nums) - 1)
    
    def merge(self, nums, start, end):
        if start < end:
            mid = (start + end) // 2
            res = self.merge(nums, start, mid) + self.merge(nums, mid + 1, end)
            j = mid + 1
            for i in xrange(start, mid + 1):
                while j <= end and nums[i] > nums[j] * 2:
                    j += 1
                res += j - (mid + 1)
            a = nums[start:mid+1]
            i = 0
            b = nums[mid+1:end+1]
            j = 0
            for idx in xrange(start, end+1):
                if i == len(a):
                    nums[idx] = b[j]
                    j += 1
                elif j == len(b):
                    nums[idx] = a[i]
                    i += 1
                elif a[i] <= b[j]:
                    nums[idx] = a[i]
                    i += 1
                else:
                    nums[idx] = b[j]
                    j += 1
            return res
        else:
            return 0
