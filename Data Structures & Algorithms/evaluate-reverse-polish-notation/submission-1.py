class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        st = []
        for i in tokens:
            if i == "+":
                b = st.pop()
                a = st.pop()
                st.append(a+b)
            elif i == "-":
                b = st.pop()
                a = st.pop()
                st.append(a-b)
            elif i == "/":
                b = st.pop()
                a = st.pop()
                st.append(int(a/b))
            elif i == "*":
                b = st.pop()
                a = st.pop()
                st.append(a*b)
            else:
                st.append(int(i))
            # print(st)
        return st.pop()