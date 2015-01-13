class Solution:
    #given a list of integers and an integer
    #return an integer
    def removeElement(self, A, elem):
        num = 0
        for i in range(len(A)):
            if A[i] == elem:
                num += 1
            else:
                A[i-num] = A[i]
        return len(A) - num
