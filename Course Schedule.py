'''
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
 Hints:

This problem is equivalent to finding if a cycle exists in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.
Topological sort could also be done via BFS.
'''

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        children_vec = {}
        parent_count = {}
        for i in xrange(numCourses):
            children_vec[i] = []
            parent_count[i] = 0
            
        for pair in prerequisites:
            children_vec[pair[1]].append(pair[0])
            parent_count[pair[0]] += 1
            
        res = []
        vec = []
        for x in parent_count:
            if parent_count[x] == 0:
                vec.append(x)
                
        while len(vec) > 0:
            next_vec = []
            for x in vec:
                res.append(x)
                for child in children_vec[x]:
                    parent_count[child] -= 1
                    if parent_count[child] == 0:
                        next_vec.append(child)
            vec = next_vec
            
        return len(res) == numCourses
