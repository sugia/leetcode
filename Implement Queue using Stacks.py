'''
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Notes:
You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
'''

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.input_stack = []
        self.output_stack = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.input_stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.output_stack:
            return self.output_stack.pop()
        else:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
                
            if self.output_stack:
                return self.output_stack.pop()
            
        return None

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.output_stack:
            return self.output_stack[-1]
        else:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
                
            if self.output_stack:
                return self.output_stack[-1]
        
        return None

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        
        return not self.output_stack and not self.input_stack

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
