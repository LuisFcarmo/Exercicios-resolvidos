from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        c:int = 0
        negativos = 0
        qtd0 = 0
        for c in nums:
            if(c > 0):
                break
            if(c < 1 and c != 0):
                negativos+=1
            else:
                qtd0 +=1
        if(negativos == 0 and len(nums)-qtd0 == 0):
            return 0
        if (len(nums)-qtd0-negativos) > negativos:
            return (len(nums)-qtd0-negativos)
        else:
            return negativos
print(Solution().maximumCount(nums = [0, 0, 0, 0]))
            