class Solution:
    def finalString(self, s: str) -> str:
        aux = ""
        for c in s:
            if(c == 'i'):
                aux = aux[::-1]
            else:
                aux += c
        return aux
print(Solution().finalString("poiinter"))