class Solution:
    def replaceDigits(self, s: str) -> str:
        aux = list()
        for c in range(len(s)):
            try:
                aux.append(chr(ord(s[c-1]) + int(s[c])))           
            except:
                aux.append(s[c])
                continue
        return "".join(aux)


Solution().replaceDigits("a1c1e1")