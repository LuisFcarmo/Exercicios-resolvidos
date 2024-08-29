def verify_palin(n, base): 
    converted = []
    while n > 0:
        converted.append(n%base)
        n //= base
    string = "".join(map(str, converted[::-1]))
    
    if(converted == string):
        return True
    return False
    
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for p in range(2, n):
            if(not verify_palin(n, p)):
                return False
        return False

print(Solution().isStrictlyPalindromic(4))