'''
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

 

Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
 

Note:

1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.

'''

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        sum_nums = sum(nums)
        if sum_nums % k != 0:
            return False
        target = sum_nums // k
        visited = [False for i in range(len(nums))]
        return self.valid(nums=nums,
                          visited=visited,
                          start=0,
                          group=k,
                          tmp_sum=0,
                          target_sum=target)
    
    def valid(self, nums: List[int], visited: List[bool], start: int, group: int, tmp_sum: int, target_sum: int):
        if group == 1:
            return True
        if tmp_sum == target_sum:
            return self.valid(nums=nums,
                              visited=visited,
                              start=0,
                              group=group-1,
                              tmp_sum=0,
                              target_sum=target_sum)
        
        for i in range(start, len(nums)):
            if visited[i]:
                continue
            
            visited[i] = True
            if self.valid(nums=nums,
                         visited=visited,
                         start=i+1,
                         group=group,
                         tmp_sum=tmp_sum+nums[i],
                         target_sum=target_sum):
                return True
            visited[i] = False
            
        return False
