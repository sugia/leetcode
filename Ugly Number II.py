'''
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:  

1 is typically treated as an ugly number.
n does not exceed 1690.
'''

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        h = [1]
        res = 0
        visited = set([1])
        for _ in range(n):
            res = heapq.heappop(h)
            if res * 2 not in visited:
                visited.add(res * 2)
                heapq.heappush(h, res * 2)
            if res * 3 not in visited:
                visited.add(res * 3)
                heapq.heappush(h, res * 3)
            if res * 5 not in visited:
                visited.add(res * 5)
                heapq.heappush(h, res * 5)
        return res
