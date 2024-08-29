class Solution:
    def buildArray(self, nums):
        arr = []
        for n in nums:
            print(n)
            arr.append(nums[n])
        return arr
    
Solution().buildArray([1, 2, 3, 4])