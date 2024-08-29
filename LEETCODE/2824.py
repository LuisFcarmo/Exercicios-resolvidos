class Solution:
    def countPairs(self, nums, target):    
        ct = 0
        for i in range(0, len(nums)):
            for k in range(i+1, len(nums)):
                if(nums[i] + nums[k] < target):
                    ct+=1
        return ct
                
print(Solution().countPairs([-1,1,2,3,1], 2))
