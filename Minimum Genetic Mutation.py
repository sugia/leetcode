'''
A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".

Suppose we need to investigate about a mutation (mutation from "start" to "end"), where ONE mutation is defined as ONE single character changed in the gene string.

For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.

Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be in the bank to make it a valid gene string.

Now, given 3 things - start, end, bank, your task is to determine what is the minimum number of mutations needed to mutate from "start" to "end". If there is no such a mutation, return -1.

Note:

Starting point is assumed to be valid, so it might not be included in the bank.
If multiple mutations are needed, all mutations during in the sequence must be valid.
You may assume start and end string is not the same.
Example 1:

start: "AACCGGTT"
end:   "AACCGGTA"
bank: ["AACCGGTA"]

return: 1
Example 2:

start: "AACCGGTT"
end:   "AAACGGTA"
bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

return: 2
Example 3:

start: "AAAAACCC"
end:   "AACCCCCC"
bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]

return: 3
'''

class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        if end not in bank:
            return -1
        dic = {}
        # build relations between start and genes in bank
        for gene in bank:
            if self.valid(start, gene):
                if start in dic:
                    dic[start].append(gene)
                else:
                    dic[start] = [gene]
                if gene in dic:
                    dic[gene].append(start)
                else:
                    dic[gene] = [start]
            
        # build relations between genes in bank
        for i in xrange(len(bank)):
            for j in xrange(i+1, len(bank)):
                if self.valid(bank[i], bank[j]):
                    if bank[i] in dic:
                        dic[bank[i]].append(bank[j])
                    else:
                        dic[bank[i]] = [bank[j]]
                    if bank[j] in dic:
                        dic[bank[j]].append(bank[i])
                    else:
                        dic[bank[j]] = [bank[i]]
                        
        # bfs
        vec = [(start, 0)]
        used = set([start])
        while vec:
            next_vec = []
            for pair in vec:
                gene = pair[0]
                count = pair[1]
                if gene not in dic:
                    continue
                for tmp in dic[gene]:
                    if tmp == end:
                        return count + 1
                    else:
                        if tmp in used:
                            continue
                        used.add(tmp)
                        next_vec.append((tmp, count+1))
                        
            vec = next_vec
            
            
        return -1
    
    def valid(self, a, b):
        if len(a) != len(b):
            return False
        count = 0
        for i in xrange(len(a)):
            if a[i] != b[i]:
                count += 1
                if count > 1:
                    return False
        if count == 1:
            return True
            
        
