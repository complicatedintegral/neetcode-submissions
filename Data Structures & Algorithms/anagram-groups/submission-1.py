class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def charCounter(s): # can also use from collections import Counter, wrote function manually to return frozenset
            d = dict()
            for i in range(len(s)):
                d[s[i]] = d.get(s[i], 0) + 1
            # print(d)
            return frozenset(d.items()) # have to frozenset d.items() to retain letters and the count of each

        d = dict()
        for i in strs:
            x = charCounter(i)
            if x not in d:
                d[x] = list()
            d[x].append(i)
            # print(d)

        return list(d.values())