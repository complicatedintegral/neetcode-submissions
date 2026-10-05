class Solution:
    def isValid(self, s: str) -> bool:

        d = {')':'(', '}': '{', ']': '['}
        st = []

        for i in s:
            if i in d:
                if st and d[i] == st[-1]:
                    st.pop()
                else:
                    return False
            else:
                st.append(i)
            # print(st)

        if not st:
            return True
        else: return False