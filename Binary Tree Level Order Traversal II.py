'''

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        
        vec = [root]
        while len(vec) > 0:
            next_vec = []
            tmp = []
            for node in vec:
                tmp.append(node.val)
                if node.left:
                    next_vec.append(node.left)
                if node.right:
                    next_vec.append(node.right)
            res = [tmp] + res
            vec = next_vec
            
        return res
            
