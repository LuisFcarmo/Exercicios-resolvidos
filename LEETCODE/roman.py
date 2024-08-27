from collections import defaultdict
class Solution:
    def romanToInt(self, s: str) -> int:
        dc = defaultdict(lambda:0)
        dc['I'] = 1
        dc['V'] = 5
        dc['X'] = 10
        dc['L'] = 50
        dc['C'] = 100
        dc['D'] = 500
        dc['M'] = 1000
        acumulador = 0
        for c in range(len(s)-1):
            if(dc[s[c]] < dc[s[c + 1]]):
                acumulador -= dc[s[c]]
                c += 1
            else:
                acumulador += dc[s[c]]
        acumulador += dc[s[-1]]
        return acumulador
    
x = Solution()
print(x.romanToInt("MCMXCIV"))