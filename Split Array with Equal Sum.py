'''
 Given an array with n integers, you need to find if there are triplets (i, j, k) which satisfies following conditions:

    0 < i, i + 1 < j, j + 1 < k < n - 1
    Sum of subarrays (0, i - 1), (i + 1, j - 1), (j + 1, k - 1) and (k + 1, n - 1) should be equal.

where we define that subarray (L, R) represents a slice of the original array starting from the element indexed L to the element indexed R.

Example:

Input: [1,2,1,2,1,2,1]
Output: True
Explanation:
i = 1, j = 3, k = 5. 
sum(0, i - 1) = sum(0, 0) = 1
sum(i + 1, j - 1) = sum(2, 2) = 1
sum(j + 1, k - 1) = sum(4, 4) = 1
sum(k + 1, n - 1) = sum(6, 6) = 1

Note:

    1 <= n <= 2000.
    Elements in the given array will be in range [-1,000,000, 1,000,000].

'''


class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        s = [nums[0]]
        count = 0
        for i in xrange(1, len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
            else:
                count = 0
            if count > 7:
                continue
            s.append(s[-1] + nums[i])
        
        for second_cut in xrange(3, len(s) - 3):
            for first_cut in xrange(1, second_cut - 1):
                if s[first_cut - 1] == s[second_cut - 1] - s[first_cut]:
                    for third_cut in xrange(second_cut + 1, len(s) - 1):
                        if s[third_cut - 1] - s[second_cut] == s[-1] - s[third_cut] == s[first_cut - 1]:
                            return True
        return False
        
