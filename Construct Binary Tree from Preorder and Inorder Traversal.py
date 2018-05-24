'''
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.build(preorder, inorder, 0)[0]
    
    def build(self, preorder, inorder, idx):
        if idx >= len(preorder):
            return None, idx
        node = TreeNode(preorder[idx])
        
        for i in xrange(len(inorder)):
            if inorder[i] == node.val:
                if 0 < i:
                    node.left, idx = self.build(preorder, inorder[:i], idx + 1)
                if i+1 < len(inorder):
                    node.right, idx = self.build(preorder, inorder[i+1:], idx + 1)
                
        return node, idx
