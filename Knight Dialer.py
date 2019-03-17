'''
A chess knight can move as indicated in the chess diagram below:

 .           

 

This time, we place our chess knight on any numbered key of a phone pad (indicated above), and the knight makes N-1 hops.  Each hop must be from one key to another numbered key.

Each time it lands on a key (including the initial placement of the knight), it presses the number of that key, pressing N digits total.

How many distinct numbers can you dial in this manner?

Since the answer may be large, output the answer modulo 10^9 + 7.

 

Example 1:

Input: 1
Output: 10
Example 2:

Input: 2
Output: 20
Example 3:

Input: 3
Output: 46
 

Note:

1 <= N <= 5000
'''

class Solution(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        nex = {1:[6, 8],    2:[7, 9], 3:[4, 8],
               4:[0, 3, 9], 5:[],     6:[0, 1, 7],
               7:[2, 6],    8:[1, 3], 9:[2, 4],
               0:[4, 6]}
        count = {}
        for i in xrange(10):
            count[i] = 1
        for _ in xrange(N-1):
            next_count = {}
            for i in xrange(10):
                next_count[i] = 0
            for i in xrange(10):
                for j in nex[i]:
                    next_count[j] += count[i]
                    next_count[j] %= 10 ** 9 + 7
            count = next_count
        return sum(count.values()) % (10 ** 9 + 7)
