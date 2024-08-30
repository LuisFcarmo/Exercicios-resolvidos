from typing import List
class Solution:
    def GetAllIndexForAnumber(self, nums: List[int], num):
        Arr = []
        for c in range(0, len(nums)):
            if(nums[c] == num):
                Arr.append(c)
        return Arr
                    
    def targetIndices(self, nums, target):
        return self.GetAllIndexForAnumber(sorted(nums), target)
        
print(Solution().targetIndices([1,2,5,2,3], 2))