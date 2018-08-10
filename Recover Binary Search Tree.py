'''
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2

Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3

Follow up:

    A solution using O(n) space is pretty straight forward.
    Could you devise a constant space solution?


'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        prev = [None]
        first = [None]
        second = [None]
        self.find(root, prev, first, second)
        
        first[0].val, second[0].val = second[0].val, first[0].val
        
    def find(self, root, prev, first, second):
        if not root:
            return
        
        self.find(root.left, prev, first, second)
        
        if prev[0]:
            if prev[0].val >= root.val:
                if not first[0]:
                    first[0] = prev[0]
                if first[0]:
                    second[0] = root
                    
        prev[0] = root
        
        self.find(root.right, prev, first, second)
        
        
