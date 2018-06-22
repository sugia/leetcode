'''
 In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.

Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

Example:

Input: [1,2,1,2,6,7,5,1], 2
Output: [0, 3, 5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.

Note:
nums.length will be between 1 and 20000.
nums[i] will be between 1 and 65535.
k will be between 1 and floor(nums.length / 3).
'''

class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        best_idx = [[0], [0, k], [0, k, 2*k]]
        best_sum = [sum(nums[:k]), sum(nums[:2*k]), sum(nums[:3*k])]
        
        window_sum = [best_sum[0], best_sum[1] - best_sum[0], best_sum[2] - best_sum[1]]
        
        for i in xrange(len(nums) - 3 * k):
            window_sum[0] = window_sum[0] - nums[i] + nums[i+k]
            window_sum[1] = window_sum[1] - nums[i+k] + nums[i+2*k]
            window_sum[2] = window_sum[2] - nums[i+2*k] + nums[i+3*k]
            
            if window_sum[0] > best_sum[0]:
                best_sum[0] = window_sum[0]
                best_idx[0] = [i+1]
                
            if window_sum[1] + best_sum[0] > best_sum[1]:
                best_sum[1] = window_sum[1] + best_sum[0]
                best_idx[1] = best_idx[0] + [i+k+1]
                
            if window_sum[2] + best_sum[1] > best_sum[2]:
                best_sum[2] = window_sum[2] + best_sum[1]
                best_idx[2] = best_idx[1] + [i+2*k+1]
                
        return best_idx[2]
