class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        nums = sorted(nums)
        begin = 0
        end = len(nums)-1
        maior = 0
        while(begin < end):
            if (nums[begin] + nums[end] > maior):
                
                maior = nums[begin] + nums[end]
            begin+=1
            end-=1
Solution().minPairSum([3,5,2,3])