'''
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:

Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4 

Output: 2
Example 2:

Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

Output:  1
Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
'''

class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        p = {}
        r = {}
        for i in xrange(n):
            p[i] = i
            r[i] = 1
        
        res = n
        for a, b in edges:
            if self.merge(a, b, p, r):
                res -= 1
        return res
    
    def merge(self, a, b, p, r):
        pa = self.get(a, p)
        pb = self.get(b, p)
        
        if pa == pb:
            return False
        
        if r[pa] < r[pb]:
            p[pa] = pb
            r[pb] += r[pa]
        else:
            p[pb] = pa
            r[pa] += r[pb]
        
        return True
    
    def get(self, a, p):
        while p[a] != p[p[a]]:
            p[a] = p[p[a]]
        return p[a]
