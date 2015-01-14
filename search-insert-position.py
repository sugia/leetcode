class Solution:
    #given a list of integers and an integer
    #return an integer
    def searchInsert(self, A, target):
        if len(A) == 0:
            return 0
        if target <= A[0]:
            return 0
        if target > A[-1]:
            return len(A)
        left = 0
        right = len(A) - 1
        while left + 1 < right:
            mid = (left + right) >> 1
            if A[mid] < target:
                left = mid
            elif A[mid] > target:
                right = mid
            else:
                return mid
        if A[left] == target:
            return left
        else:
            return right
