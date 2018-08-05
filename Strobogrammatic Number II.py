'''
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

Example:

Input:  n = 2
Output: ["11","69","88","96"]


'''

class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        '''
        1 = 1
        6 = 9
        8 = 8
        9 = 6
        0 = 0
        '''
        
        res = []
        tmp = ['' for i in xrange(n)]
        pairs = {1:1, 6:9, 8:8, 9:6, 0:0}
        
        self.find(pairs, 0, n - 1, tmp, res)
        
        return res
    
    def find(self, pairs, start, end, tmp, res):
        if start == end:
            for i in [0, 1, 8]:
                tmp[start] = i
                res.append(''.join([str(x) for x in tmp]))
        elif start > end:
            res.append(''.join([str(x) for x in tmp]))
        else:
            for k, v in pairs.iteritems():
                if start == 0 and k == 0:
                    continue
                tmp[start] = k
                tmp[end] = v
                self.find(pairs, start + 1, end - 1, tmp, res)
                
