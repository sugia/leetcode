class Solution:
    #given a list of integers and an integer
    #return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        left = 0
        right = len(A) - 1
        while left + 1 < right:
            mid = (left + right) >> 1
            if A[mid] < target:
                left = mid
            elif A[mid] > target:
                right = mid
            else:
                right = mid
        idx = -1
        if A[left] == target:
            idx = left
        elif A[right] == target:
            idx = right
        else:
            return [-1, -1]
        left = 0
        right = len(A) - 1
        while left + 1 < right:
            mid = (left + right) >> 1
            if A[mid] < target:
                left = mid
            elif A[mid] > target:
                right = mid
            else:
                left = mid
        if A[right] == target:
            return [idx, right]
        else:
            return [idx, left]
