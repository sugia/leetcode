class Solution:
    #given a list of integers
    #return an integer
    def removeDuplicates(self, A):
        num = 0
        for i in range(1, len(A)):
            if A[i] == A[i-1-num]:
                num += 1
            A[i-num] = A[i]
        return len(A) - num
