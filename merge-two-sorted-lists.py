'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''
class Solution:
    #given two list nodes
    #return one list node
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        p = dummy
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        if l1:
            p.next = l1
        elif l2:
            p.next = l2
        return dummy.next
