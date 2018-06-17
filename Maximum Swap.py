'''
 Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:

Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Example 2:

Input: 9973
Output: 9973
Explanation: No swap.

Note:

    The given number is in the range [0, 108]

'''

class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        vec = list(str(num))
        
        max_val_idx_from_right = [0 for i in xrange(len(vec))]
        
        max_val_idx_from_right[-1] = len(vec) - 1
        for i in reversed(xrange(len(vec) - 1)):
            if vec[i] > vec[max_val_idx_from_right[i+1]]:
                max_val_idx_from_right[i] = i
            else:
                max_val_idx_from_right[i] = max_val_idx_from_right[i+1]
        
        for i in xrange(len(vec)):
            if vec[max_val_idx_from_right[i]] > vec[i]:
                vec[i], vec[max_val_idx_from_right[i]] = vec[max_val_idx_from_right[i]], vec[i]
                break
                
        return int(''.join(vec))
