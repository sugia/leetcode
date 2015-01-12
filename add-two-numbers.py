'''
def ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''

class Solution:
    #given two list nodes
    #return one list node
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        p = dummy
        carry = 0
        while l1 or l2:
            x = 0
            if l1:
                x = l1.val
                l1 = l1.next
            y = 0
            if l2:
                y = l2.val
                l2 = l2.next
            tmp = carry + x + y
            carry = tmp // 10
            tmp %= 10
            q = ListNode(tmp)
            p.next = q
            p = p.next
        if carry:
            q = ListNode(carry)
            p.next = q
        return dummy.next
