class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        st = []
        str2 = []
        qtd = 0
        if(x>0):
            st.append("0")
        else:
            st.append("1")
        if(y>0):
            str2.append("0")
        else:
            str2.append("1")
        while(x > 0):
            if(x%2 == 0):
                st.append("0")
            else:
                st.append("1")
            x //= 2
        while(y > 0):
            if(y%2 == 0):
                str2.append("0")
            else:
                str2.append("1")
            y //= 2
        while(len(st) != len(str2)):
            str2.append("0")
        while(len(str2) != len(st)):
            st.append("0")
        for c in range(len(st)):
            if(st[c] != str2[c]):
                qtd+=1
        return qtd     
print(Solution().hammingDistance(3, 1))