'''
You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.

Example:
Input: "4(2(3)(1))(6(5))"
Output: return the tree root node representing the following tree:

       4
     /   \
    2     6
   / \   / 
  3   1 5   
Note:
There will only be '(', ')', '-' and '0' ~ '9' in the input string.
An empty tree is represented by "" instead of "()".
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        if s:
            left = -1
            count = 0
            right = -1
            for i in xrange(len(s)):
                if s[i] == '(':
                    count += 1
                    if left == -1:
                        left = i
                elif s[i] == ')':
                    count -= 1
                    if count == 0 and right == -1:
                        right = i

            if left != -1:
                node = TreeNode(int(s[:left]))
            else:
                node = TreeNode(s)
            if left != -1 and right != -1:
                node.left = self.str2tree(s[left+1:right]) 
                node.right = self.str2tree(s[right+2:-1])
            
            return node
        else:
            return None
