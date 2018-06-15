'''
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples 1:

Input: [3,9,20,null,null,15,7]

   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7 

Output:

[
  [9],
  [3,15],
  [20],
  [7]
]

Examples 2:

Input: [3,9,8,4,0,1,7]

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7 

Output:

[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]

Examples 3:

Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2

Output:

[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]


'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        
        idx_val = {}
        min_idx = 0
        max_idx = 0
        vec = [(root, 0)]
        while vec:
            next_vec = []
            for (node, col) in vec:
                if col not in idx_val:
                    idx_val[col] = [node.val]
                else:
                    idx_val[col].append(node.val)
                
                min_idx = min(min_idx, col)
                max_idx = max(max_idx, col)
                
                if node.left:
                    next_vec.append((node.left, col-1))
                if node.right:
                    next_vec.append((node.right, col+1))
                    
            vec = next_vec
        
        for idx in xrange(min_idx, max_idx + 1):
            res.append(idx_val[idx])
            
        return res
