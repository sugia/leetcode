'''
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None:
            return
        
        fast, slow, slow_prev = head, head, None
        while fast and fast.next:
            fast, slow, slow_prev = fast.next.next, slow.next, slow
        
        slow_prev.next = None
        last_node = slow
        while last_node and last_node.next:
            last_node = last_node.next

        self.reverse(slow, last_node)

        dummy = ListNode(0)
        cur = dummy
        while head or last_node:
            if head:
                cur.next = head
                cur = cur.next
                head = head.next
            if last_node:
                cur.next = last_node
                cur = cur.next
                last_node = last_node.next
                
        head = dummy.next
    
    def reverse(self, head, tail):
        x = head
        y = x.next
        while y:
            z = y.next
            y.next = x
            x = y
            y = z
        head.next = None
