'''
Implement a data structure supporting the following operations:

    Inc(Key) - Inserts a new key with value 1. Or increments an existing key by 1. Key is guaranteed to be a non-empty string.
    Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. If the key does not exist, this function does nothing. Key is guaranteed to be a non-empty string.
    GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string "".
    GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string "".

Challenge: Perform all these in O(1) time complexity. 
'''

class Node:
    def __init__(self, key='', val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # key to node
        self.dic = {}
        
        self.head = Node(key='head', val=float('-inf'))
        self.tail = Node(key='tail', val=float('inf'))
        self.head.next = self.tail
        self.tail.prev = self.head

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key not in self.dic:
            self.dic[key] = Node(key=key, val=1)
            self.addLink(self.dic[key], self.head)
        else:
            self.dic[key].val += 1
            prev = self.dic[key].prev
            self.removeLink(self.dic[key])
            while prev.val < self.dic[key].val:
                prev = prev.next
            
            self.addLink(self.dic[key], prev.prev)
        
        # self.display('-----inc {}'.format(key))
        
            
    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key not in self.dic:
            return
        
        self.dic[key].val -= 1
        if self.dic[key].val == 0:
            self.removeLink(self.dic[key])
            del self.dic[key]
        else:
            next = self.dic[key].next
            self.removeLink(self.dic[key])
            while self.dic[key].val < next.val:
                next = next.prev
            self.addLink(self.dic[key], next)
        
        # self.display('-----dec {}'.format(key))
            
    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        if self.head.next == self.tail:
            return ''
        return self.tail.prev.key

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        if self.head.next == self.tail:
            return ''
        return self.head.next.key

    def addLink(self, node: Node, prev: Node) -> None:
        next = prev.next
        
        node.prev = prev
        node.next = next
        prev.next = node
        next.prev = node
    
    def removeLink(self, node: Node) -> None:
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        
    def display(self, s: str) -> None:
        print(s)
        node = self.head.next
        while node != self.tail:
            print(node.key, node.val)
            node = node.next
        
# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
