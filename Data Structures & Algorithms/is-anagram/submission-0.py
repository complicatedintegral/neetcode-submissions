class Solution:

    def isAnagram(self, s: str, t: str) -> bool:

        def dictStr(s: str):
            d = dict()
            for i in range(len(s)):
                if s[i] not in d:
                    d[s[i]] = 1
                else:
                    d[s[i]] += 1

            return d
        
        d1 = dictStr(s)
        d2 = dictStr(t)

        if d1 == d2:
            return True
        else:
            return False