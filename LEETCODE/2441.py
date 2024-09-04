class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        nums = sorted(nums)
        end =len(nums)-1
        begin = 0
        print(nums)
        while (begin < end):
            if(nums[end] == nums[begin]*-1):
                return nums[end]
            if(nums[end] > nums[begin]*-1):
                end-=1
            if(nums[end] < nums[begin]*-1):
                print(nums[begin])
                begin+=1
        return -1
print(Solution().findMaxK([14,33,40,-33,8,-24,-42,30,-18,-34]))