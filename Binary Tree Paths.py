'''
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        
        res = []
        if not root:
            return res
        self.find(root, [], res)
        return res
    
    def find(self, node, tmp, res):
        if node.left:
            if node.right:
                self.find(node.left, tmp + [str(node.val)], res)
                self.find(node.right, tmp + [str(node.val)], res)
            else:
                self.find(node.left, tmp + [str(node.val)], res)
        else:
            if node.right:
                self.find(node.right, tmp + [str(node.val)], res)
            else:
                res.append('->'.join(tmp + [str(node.val)]))
