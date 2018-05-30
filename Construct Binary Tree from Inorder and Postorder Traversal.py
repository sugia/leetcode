'''
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
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
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.build(inorder, postorder, len(postorder) - 1)[0]
    
    def build(self, inorder, postorder, idx):
        if len(inorder) == 0 or idx < 0:
            return None, idx
        node = TreeNode(postorder[idx])
        for i in xrange(len(inorder)):
            if inorder[i] == postorder[idx]:
                if inorder[i+1:]:
                    node.right, idx = self.build(inorder[i+1:], postorder, idx - 1)
                if inorder[:i]:
                    node.left, idx = self.build(inorder[:i], postorder, idx - 1)
                break
        return node, idx
                
