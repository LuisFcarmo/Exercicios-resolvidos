class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s.split(" ")
        st = ""
        for c in range(k):
            if(c == k):
                st += s[c]
            else:
                st += s[c]
                st += " "
        return st