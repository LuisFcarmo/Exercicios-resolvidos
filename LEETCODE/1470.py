from typing import List
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        fatiada = nums[0:n]
        fatiada2 = nums[n:len(nums)]
        merge = [item for pair in zip(fatiada, fatiada2) for item in pair]
        return merge
print(Solution().shuffle([2,5,1,3,4,7], 3))