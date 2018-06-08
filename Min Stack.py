'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        # (val, current_min)
        self.vec = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.vec:
            self.vec.append((x, x))
        else:
            self.vec.append((x, min(x, self.vec[-1][1])))

    def pop(self):
        """
        :rtype: void
        """
        if not self.vec:
            return
        self.vec.pop()

    def top(self):
        """
        :rtype: int
        """
        if not self.vec:
            raise 'Error: min stack is empty'
        
        return self.vec[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.vec:
            raise 'Error: min stack is empty'
            
        return self.vec[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
