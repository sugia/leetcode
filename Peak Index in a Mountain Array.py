'''
Let's call an array A a mountain if the following properties hold:

    A.length >= 3
    There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]

Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:

Input: [0,1,0]
Output: 1

Example 2:

Input: [0,2,1,0]
Output: 1

Note:

    3 <= A.length <= 10000
    0 <= A[i] <= 10^6
    A is a mountain, as defined above.


'''

class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        left = [False for i in xrange(len(A))]
        for i in xrange(1, len(A)):
            if A[i-1] < A[i]:
                left[i] = True
            else:
                break
                
        right = [False for i in xrange(len(A))]
        for i in reversed(xrange(0, len(A) - 1)):
            if A[i] > A[i+1]:
                right[i] = True
            else:
                break
                
        for i in xrange(1, len(A) - 1):
            if left[i] and right[i]:
                return i
            
        return -1
