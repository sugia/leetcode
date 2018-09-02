'''
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0] 
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
'''

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        res = [0 for i in xrange(len(nums))]
        vec = [(i, v) for i, v in enumerate(nums)]
        self.mergeSort(vec, 0, len(vec)-1, res)
        return res
    
    def mergeSort(self, vec, left, right, res):
        if left < right:
            mid = (left + right) // 2
            self.mergeSort(vec, left, mid, res)
            self.mergeSort(vec, mid+1, right, res)
            j = mid + 1
            for i in xrange(left, mid+1):
                while j <= right and vec[i][1] > vec[j][1]:
                    j += 1
                res[vec[i][0]] += j - (mid + 1)
            
            a = vec[left:mid+1]
            b = vec[mid+1:right+1]
            i = 0
            j = 0
            for idx in xrange(left, right+1):
                if i >= len(a):
                    vec[idx] = b[j]
                    j += 1
                elif j >= len(b):
                    vec[idx] = a[i]
                    i += 1
                else:
                    if a[i][1] <= b[j][1]:
                        vec[idx] = a[i]
                        i += 1
                    else:
                        vec[idx] = b[j]
                        j += 1
                        
            
