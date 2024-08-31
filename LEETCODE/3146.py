class md:
    @staticmethod
    def md_meu(num):
        if num < 0: return num*-1
        else:return num
        
class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        total = 0
        for c in s:
           total += md.md_meu(s.index(c) - t.index(c))
        return total

print(Solution().findPermutationDifference("abc", "bac"))