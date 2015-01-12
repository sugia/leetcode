class Solution:
    #given two lists of integers
    #return an integer
    def findMedianSortedArrays(self, A, B):
        clen = len(A) + len(B)
        if clen & 1:
            return self.cal(A, B, (clen >> 1) + 1)
        else:
            return 0.5 * (self.cal(A, B, (clen >> 1)) + self.cal(A, B, (clen >> 1) + 1))
    def cal(self, A, B, k):
        if len(A) > len(B):
            return self.cal(B, A, k)
        if len(A) == 0:
            return B[k-1]
        if k == 1:
            return min(A[0], B[0])
        pa = min(k >> 1, len(A))
        pb = k - pa
        if A[pa-1] < B[pb-1]:
            return self.cal(A[pa:], B, k - pa)
        else:
            return self.cal(A, B[pb:], k - pb)
