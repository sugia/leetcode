'''
 Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 

The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction. 
'''

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        dic = {}
        for i in xrange(len(equations)):
            a = equations[i][0]
            b = equations[i][1]
            k = values[i]
            
            if a not in dic:
                dic[a] = {}
            dic[a][a] = 1.0
            dic[a][b] = 1.0 / k
            
            if b not in dic:
                dic[b] = {}
            dic[b][b] = 1.0
            dic[b][a] = k
        
        for a in dic:
            for c in dic:
                for b in dic:
                    if b in dic[a] and c in dic[b]:
                        dic[a][c] = dic[a][b] * dic[b][c]
                        
        res = []
        for a, b in queries:
            if b in dic and a in dic[b]:
                res.append(dic[b][a])
            else:
                res.append(-1.0)
        
        return res
