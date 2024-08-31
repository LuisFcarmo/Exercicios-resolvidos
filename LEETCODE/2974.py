from typing import List

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        return nums[::-1]
Solution().numberGame([5,4,2,3])