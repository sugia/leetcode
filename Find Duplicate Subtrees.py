'''
Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

Example 1:

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
The following are two duplicate subtrees:

      2
     /
    4
and

    4
Therefore, you need to return above trees' root in the form of a list.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        
        dic = {}
        self.find(root, dic)
        
        res = []
        for k, v in dic.iteritems():
            if len(v) > 1:
                res.append(v[0])
        return res
    
    def find(self, node, dic):
        if not node:
            return ''
        key = ' '.join([str(node.val), self.find(node.left, dic), self.find(node.right, dic)])
        if key in dic:
            dic[key].append(node)
        else:
            dic[key] = [node]
        return key
