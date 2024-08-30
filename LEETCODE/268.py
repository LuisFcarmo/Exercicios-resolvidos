from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ct = 0
        while True:
            try:
                nums.index(ct)
                ct+=1
            except:
                return ct
print(Solution().missingNumber([3,0,1]))