'''
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.


Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
'''

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        '''
        [[4, 4], [5, 0], [5, 2], [6, 1], [7, 0], [7, 1]]
        [[4, 4], [5, 0], [5, 2], [7, 0], [6, 1], [7, 1]]
        [[4, 4], [5, 0], [7, 0], [5, 2], [6, 1], [7, 1]]
        [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
        '''
        
        res = sorted(people, key = lambda x: (x[0], x[1]))
        
        for i in reversed(xrange(len(res))):
            j = i
            while j - 1 >= 0 and res[j-1][0] >= res[i][0]:
                j -= 1
            step = res[i][1] - (i - j)
            res = res[:i] + res[i+1:i+1+step] + [res[i]] + res[i+1+step:]
            
        return res
            
