class Solution:
    def isArraySpecial(self, nums: list[int]) -> bool:
        for c in range(len(nums)-1):
            if(nums[c] % 2 == 0 and nums[c+1]%2 == 0):
                return False
            elif(nums[c] % 2 != 0 and nums[c+1]%2 != 0):
                return False
        return True
print(Solution().isArraySpecial([4,3,1,6]))