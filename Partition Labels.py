'''
 A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

Note:

    S will have length in range [1, 500].
    S will consist of lowercase letters ('a' to 'z') only.

'''

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        
        dic = {}
        for i in xrange(len(S)):
            if S[i] in dic:
                dic[S[i]].append(i)
            else:
                dic[S[i]] = [i]
                
        vec = []
        for key in dic:
            vec.append([dic[key][0], dic[key][-1]])
            
        vec.sort(key = lambda x: (x[0], x[1]))
        
        res = [vec[0]]
        for i in xrange(1, len(vec)):
            if vec[i][0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], vec[i][1])
            else:
                res.append(vec[i])
                
        ans = []
        for x in res:
            ans.append(x[1] - x[0] + 1)
            
        return ans
