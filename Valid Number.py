'''
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button to reset your code definition.

'''

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        idx = s.find('e')
        if idx == -1:
            return self.valid(s, allow_dot = True, allow_empty_prefix = True, allow_empty_suffix = True)
        else:
            return self.valid(s[:idx], allow_dot = True, allow_empty_prefix = True, allow_empty_suffix = False) and self.valid(s[idx+1:], allow_dot = False, allow_empty_prefix = False, allow_empty_suffix = True)
        
    def valid(self, s, allow_dot=True, allow_empty_prefix=True, allow_empty_suffix=True):
        # remove empty space at the beginning of s
        if allow_empty_prefix:
            while s and s[0] == ' ':
                s = s[1:]
        
        # remove '+' or '-' at the beginning of s
        if s and s[0] in set(['+', '-']):
            s = s[1:]
            
        # remove empty space at the end of s
        if allow_empty_suffix:
            while s and s[-1] == ' ':
                s = s[:-1]
            
        digit_count = 0
        dot_count = 0
        
        for c in s:
            if c == '.':
                if not allow_dot or dot_count > 0:
                    return False
                dot_count += 1
            elif c.isdigit():
                digit_count += 1
            else:
                return False
            
        return digit_count > 0
        
