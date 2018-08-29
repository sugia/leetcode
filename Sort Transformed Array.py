'''
 Given a sorted array of integers nums and integer values a, b and c. Apply a quadratic function of the form f(x) = ax2 + bx + c to each element x in the array.

The returned array must be in sorted order.

Expected time complexity: O(n)

Example:

nums = [-4, -2, 2, 4], a = 1, b = 3, c = 5,

Result: [3, 9, 15, 33]

nums = [-4, -2, 2, 4], a = -1, b = 3, c = 5

Result: [-23, -5, 1, 7]

'''

class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        if a == 0:
            if b == 0:
                return [c for i in xrange(len(nums))]
            elif b > 0:
                return [b * x + c for x in nums]
            else:
                # b < 0
                return [b * x + c for x in reversed(nums)]
        elif a > 0:
            mid = -b / (2.0 * a)
            i = 0
            j = len(nums) - 1
            res = []
            while i <= j:
                if abs(nums[i] - mid) > abs(nums[j] - mid):
                    res = [self.f(nums[i], a, b, c)] + res
                    i += 1
                else:
                    res = [self.f(nums[j], a, b, c)] + res
                    j -= 1
            return res
        else:
            # a < 0
            mid = -b / (2.0 * a)
            i = 0
            j = len(nums) - 1
            res = []
            while i <= j:
                if (abs(nums[i] - mid) > abs(nums[j] - mid)):
                    res.append(self.f(nums[i], a, b, c))
                    i += 1
                else:
                    res.append(self.f(nums[j], a, b, c))
                    j -= 1
            return res
    def f(self, x, a, b, c):
        return a * x * x + b * x + c
