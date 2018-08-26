'''
Implement a data structure supporting the following operations:

    Inc(Key) - Inserts a new key with value 1. Or increments an existing key by 1. Key is guaranteed to be a non-empty string.
    Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. If the key does not exist, this function does nothing. Key is guaranteed to be a non-empty string.
    GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string "".
    GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string "".

Challenge: Perform all these in O(1) time complexity. 
'''

class AllOne(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.kv = {}
        self.maxk = ''
        self.maxv = float('-inf')
        self.mink = ''
        self.minv = float('inf')
        
    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        if key in self.kv:
            self.kv[key] += 1
        else:
            self.kv[key] = 1
            
        if self.mink == key:
            self.mink = ''
            self.minv = float('inf')
        elif self.minv > self.kv[key]:
            self.mink = key
            self.minv = self.kv[key]
            
        if self.maxv < self.kv[key]:
            self.maxk = key
            self.maxv = self.kv[key]

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        
        if key in self.kv:
            self.kv[key] -= 1
            if self.kv[key] == 0:
                del self.kv[key]
                
                if self.maxk == key:
                    self.maxk = ''
                    self.maxv = float('-inf')
                if self.mink == key:
                    self.mink = ''
                    self.minv = float('inf')
            else:
                if self.maxk == key:
                    self.maxk = ''
                    self.maxv = float('-inf')
                elif self.maxv < self.kv[key]:
                    self.maxk = key
                    self.maxv = self.kv[key]
                
                if self.minv > self.kv[key]:
                    self.mink = key
                    self.minv = self.kv[key]
        
    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if self.maxk:
            return self.maxk
        else:
            if self.kv:
                for k, v in self.kv.iteritems():
                    if v > self.maxv:
                        self.maxk = k
                        self.maxv = v
                return self.maxk
            else:
                return ''


    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if self.mink:
            return self.mink
        else:
            if self.kv:
                for k, v in self.kv.iteritems():
                    if v < self.minv:
                        self.mink = k
                        self.minv = v
                return self.mink
            else:
                return ''


        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
