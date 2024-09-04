class Solution:
    def minimumAverage(self, nums: list[int]) -> float:
        nums = sorted(nums)
        begin = 0
        end = len(nums)-1
        value = 0
        menor = nums[end]
        while (begin < end):
            value = (nums[begin] + nums[end])/2
            begin += 1
            end-=1
            if(value < menor):
                menor = value
        return menor
print(Solution().minimumAverage([7,8,3,4,15,13,4,1]))