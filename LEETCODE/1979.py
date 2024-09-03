from typing import List
from math import gcd
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mn = min(nums)
        mx = max(nums)
        return gcd(mn, mx)
print(Solution().findGCD([2,5,6,9,10]))