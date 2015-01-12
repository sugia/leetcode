'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''

class Solution:
    #given a list node and an integer
    #return a list node
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        for i in range(n):
            p = p.next
        q = dummy
        while p.next:
            p = p.next
            q = q.next
        tmp = q.next
        q.next = q.next.next
        del tmp
        return dummy.next
