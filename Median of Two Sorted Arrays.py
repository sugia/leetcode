'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

 

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5


'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        nums1 = [float('-inf')] + nums1 + [float('inf')]
        nums2 = [float('-inf')] + nums2 + [float('inf')]
        
        l = len(nums1) + len(nums2)
        k = (l + 1) // 2
        
        
        left = 0
        right = len(nums1) - 1
        while left <= right:
            mid = (left + right) // 2
            idx = k - (mid + 1) - 1
            
            if max(nums1[mid], nums2[idx]) <= min(nums1[mid+1], nums2[idx+1]):
                if l & 1:
                    return max(nums1[mid], nums2[idx]) * 1.0
                else:
                    return (max(nums1[mid], nums2[idx]) + min(nums1[mid+1], nums2[idx+1])) * 0.5
            else:
                if nums1[mid] < nums2[idx]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
