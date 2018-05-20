'''

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example: 

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
Clarification: Just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.


'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        vec = []
        self.serializeHelper(root, vec)
        return ' '.join(vec)
    
    def serializeHelper(self, node, vec):
        if not node:
            vec.append('#')
            return
        vec.append(str(node.val))
        self.serializeHelper(node.left, vec)
        self.serializeHelper(node.right, vec)
        
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vec = data.split(' ')
        
        return self.deserializeHelper(vec, 0)[0]
    
    def deserializeHelper(self, vec, idx):
        if not vec:
            return None, idx
        
        if vec[idx] == '#':
            return None, idx
        
        root = TreeNode(int(vec[idx]))
        root.left, idx = self.deserializeHelper(vec, idx + 1)
        root.right, idx = self.deserializeHelper(vec, idx + 1)
        return root, idx

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
