'''
Given a chemical formula (given as a string), return the count of each atom.

An atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

1 or more digits representing the count of that element may follow if the count is greater than 1. If the count is 1, no digits will follow. For example, H2O and H2O2 are possible, but H1O2 is impossible.

Two formulas concatenated together produce another formula. For example, H2O2He3Mg4 is also a formula.

A formula placed in parentheses, and a count (optionally added) is also a formula. For example, (H2O2) and (H2O2)3 are formulas.

Given a formula, output the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

Example 1:
Input: 
formula = "H2O"
Output: "H2O"
Explanation: 
The count of elements are {'H': 2, 'O': 1}.
Example 2:
Input: 
formula = "Mg(OH)2"
Output: "H2MgO2"
Explanation: 
The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
Example 3:
Input: 
formula = "K4(ON(SO3)2)2"
Output: "K4N2O14S4"
Explanation: 
The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
Note:

All atom names consist of lowercase letters, except for the first character which is uppercase.
The length of formula will be in the range [1, 1000].
formula will only consist of letters, digits, and round parentheses, and is a valid formula as defined in the problem.
'''

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        vec = []
        for c in formula:
            if c.isupper():
                vec.append(c)
            elif c.islower():
                vec[-1] += c
            elif c.isdigit():
                if vec and vec[-1].isdigit():
                    vec[-1] += c
                else:
                    vec.append(c)
            elif c == '(' or c == ')':
                vec.append(c)
                

        stack = []
        for c in vec:
            if c == '(' or c == ')':
                stack.append(c)
            elif c.isalpha():
                stack.append([c, 1])
            elif c.isdigit():
                if stack[-1] == ')':
                    count = 1
                    idx = len(stack) - 1
                    while count > 0:
                        idx -= 1
                        if stack[idx] == ')':
                            count += 1
                        elif stack[idx] == '(':
                            count -= 1
                        else:
                            stack[idx][1] *= int(c)
                else:
                    stack[-1][1] *= int(c)
        
        dic = {}
        for c in stack:
            if c == '(' or c == ')':
                continue
            key, value = c
            if key not in dic:
                dic[key] = 0
            dic[key] += value
        
        res = ''
        for key in sorted(dic.keys()):
            if dic[key] == 1:
                res += key
            else:
                res += key + str(dic[key])
        
        return res
        
