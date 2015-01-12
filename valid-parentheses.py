class Solution:
    #given a string
    #return a bool
    def isValid(self, s):
        stack = []
        for x in s:
            if x in '([{':
                stack.append(x)
            else:
                if len(stack) == 0:
                    return False
                if stack[-1] == '(' and x == ')':
                    stack.pop()
                elif stack[-1] == '[' and x == ']':
                    stack.pop()
                elif stack[-1] == '{' and x == '}':
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
