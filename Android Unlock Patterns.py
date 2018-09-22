'''
Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤ n ≤ 9, count the total number of unlock patterns of the Android lock screen, which consist of minimum of m keys and maximum n keys.

Rules for a valid pattern:

Each pattern must connect at least m keys and at most n keys.
All the keys must be distinct.
If the line connecting two consecutive keys in the pattern passes through any other keys, the other keys must have previously selected in the pattern. No jumps through non selected key is allowed.
The order of keys used matters.
 


Explanation:

| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
Invalid move: 4 - 1 - 3 - 6 
Line 1 - 3 passes through key 2 which had not been selected in the pattern.

Invalid move: 4 - 1 - 9 - 2
Line 1 - 9 passes through key 5 which had not been selected in the pattern.

Valid move: 2 - 4 - 1 - 3 - 6
Line 1 - 3 is valid because it passes through key 2, which had been selected in the pattern

Valid move: 6 - 5 - 4 - 1 - 9 - 2
Line 1 - 9 is valid because it passes through key 5, which had been selected in the pattern.

Example:

Input: m = 1, n = 1
Output: 9
'''

class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dic = {(1, 3):2, (3, 1):2, (1, 7):4, (7, 1):4, (3, 9):6, (9, 3):6, (7, 9):8, (9, 7):8, (1, 9): 5, (9, 1):5, (2, 8):5, (8, 2):5, (3, 7):5, (7, 3):5, (4, 6):5, (6, 4):5}
        
        res = 0
        for step in xrange(m, n+1):
            res += 4 * self.find(1, step-1, dic, set())
            res += 4 * self.find(2, step-1, dic, set())
            res += self.find(5, step-1, dic, set())
        return res
    
    def find(self, x, step, dic, visited):
        if step == 0:
            return 1
        visited.add(x)
        res = 0
        for y in xrange(1, 10):
            if y not in visited and ((x, y) not in dic or dic[(x, y)] in visited):
                res += self.find(y, step-1, dic, visited)
        
        visited.remove(x)
        return res
            
    
        
