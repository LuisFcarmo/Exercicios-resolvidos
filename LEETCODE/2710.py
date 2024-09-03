class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        num = num[::-1]
        limit = 0
        for c in num:
            if(c != "0"):
                break
            limit+=1
        num = num[::-1]
        return num[0: len(num)-limit]
print(Solution().removeTrailingZeros("51230100"))