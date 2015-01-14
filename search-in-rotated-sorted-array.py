class Solution:
    #given a list of integers and an integer
    #return an integer
    def search(self, A, target):
        left = 0
        right = len(A) - 1
        while left + 1 < right:
            mid = (left + right) >> 1
            if A[left] <= A[mid]:
                if A[left] <= target <= A[mid]:
                    right = mid
                else:
                    left = mid
            else:
                if A[mid] <= target <= A[right]:
                    left = mid
                else:
                    right = mid
        if A[left] == target:
            return left
        elif A[right] == target:
            return right
        else:
            return -1
