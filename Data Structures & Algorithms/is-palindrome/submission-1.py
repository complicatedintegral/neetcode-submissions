class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        t = ""

        for i in s: # ensuring string only contains lowercase characters
            if i.isalnum(): # only included alphabetical characters first
                if i.isupper():
                    t += i.lower()
                else:
                    t += i
        print(t)
        i = 0
        j = len(t) - 1

        while i < j:
            if t[i] != t[j]:
                return False

            i += 1
            j -= 1

        return True