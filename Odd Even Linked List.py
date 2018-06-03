'''
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
Note:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd_dummy = ListNode(0)
        odd_cur = odd_dummy
        even_dummy = ListNode(0)
        even_cur = even_dummy
        
        cur = head
        count = 0
        while cur:
            count += 1
            if count & 1:
                odd_cur.next = cur
                odd_cur = odd_cur.next
            else:
                even_cur.next = cur
                even_cur = even_cur.next
            cur = cur.next
            
        odd_cur.next = even_dummy.next
        even_cur.next = None
        
        return odd_dummy.next
        
                
