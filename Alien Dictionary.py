'''
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"
Example 3:

Input:
[
  "z",
  "x",
  "z"
] 

Output: "" 

Explanation: The order is invalid, so return "".
Note:

You may assume all letters are in lowercase.
You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
'''

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        parent_count = {}
        children = {}
        char_set = set()
        for word in words:
            for c in word:
                parent_count[c] = 0
                char_set.add(c)
                
        for i in xrange(len(words)):
            for j in xrange(i+1, len(words)):
                for k in xrange(min(len(words[i]), len(words[j]))):
                    if words[i][k] != words[j][k]:
                        if words[i][k] not in children:
                            children[words[i][k]] = [words[j][k]]
                            if words[j][k] not in parent_count:
                                parent_count[words[j][k]] = 1
                            else:
                                parent_count[words[j][k]] += 1
                        else:
                            if words[j][k] not in children[words[i][k]]:
                                children[words[i][k]].append(words[j][k])
                                if words[j][k] not in parent_count:
                                    parent_count[words[j][k]] = 1
                                else:
                                    parent_count[words[j][k]] += 1
                        break
                            
        
        res = []
        vec = []
        for k in parent_count:
            if parent_count[k] == 0:
                vec.append(k)
                
        while vec:
            next_vec = []
            for c in vec:
                res.append(c)
                if c in children:
                    for child in children[c]:
                        parent_count[child] -= 1
                        if parent_count[child] == 0:
                            next_vec.append(child)
            vec = next_vec
            
        if len(res) != len(char_set):
            return ''
        return ''.join(res)
