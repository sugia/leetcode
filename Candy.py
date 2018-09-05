'''
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Example 1:

Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
             The third child gets 1 candy because it satisfies the above two conditions.
'''

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        res = [1 for i in xrange(len(ratings))]
        h = []
        for i in xrange(len(ratings)):
            heapq.heappush(h, (ratings[i], i))
        while h:
            v, i = heapq.heappop(h)
            if 0 <= i-1:
                if ratings[i-1] < ratings[i]:
                    res[i] = max(res[i], res[i-1]+1)
            if i+1 < len(ratings):
                if ratings[i] > ratings[i+1]:
                    res[i] = max(res[i], res[i+1]+1)
        return sum(res)
