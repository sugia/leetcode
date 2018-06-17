'''
Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Example 1:

Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true

Example 2:

Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false

Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.

'''

class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        
        p = [i for i in xrange(n)]
        r = [1 for i in xrange(n)]
        
        for edge in edges:
            if not self.merge(edge[0], edge[1], p, r):
                return False
            
        box = set()
        for i in xrange(n):
            box.add(self.getp(i, p))
            
        return len(box) == 1
    
    def merge(self, a, b, p, r):
        pa = self.getp(a, p)
        pb = self.getp(b, p)
        
        if pa == pb:
            return False
        
        if r[pa] > r[pb]:
            p[pb] = p[pa]
            r[pa] += r[pb]
        else:
            p[pa] = p[pb]
            r[pb] += r[pa]
            
        return True
    
    def getp(self, x, p):
        while p[x] != p[p[x]]:
            p[x] = p[p[x]]
        
        return p[x]
            
