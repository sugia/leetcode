'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

'''

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        p = {}
        for num in nums:
            p[num] = num
        rank = {}
        for num in nums:
            rank[num] = 1
        
        exists = set()

        for num in nums:
            if num in exists:
                continue
            if num - 1 in exists:
                self.union(num - 1, num, p, rank)

            if num + 1 in exists:
                self.union(num, num + 1, p, rank)

            exists.add(num)
            
        res = 0
        for key in rank:
            res = max(res, rank[key])

        return res
    
    def union(self, a, b, p, rank):
        pa = self.getp(a, p)
        pb = self.getp(b, p)
        
        if rank[pa] < rank[pb]:
            p[pa] = pb
            rank[pb] += rank[pa]
        else:
            p[pb] = pa
            rank[pa] += rank[pb]
            
    def getp(self, x, p):
        while p[x] != p[p[x]]:
            p[x] = p[p[x]]
        return p[x]
            
