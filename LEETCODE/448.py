class Solution:
    def findDisappearedNumbers(self, nums):
        nums = sorted(nums)
        arr = list()
        vet = (nums[len(nums)-1]+1)*[0]
        for n in nums:
            vet[n] += 1
        
        for n in range(0, len(vet)):
            if (vet[n] == 0):
                arr.append(n)
        
        if(vet[len(nums)-1]==0):
            arr.append(len(nums))
        return arr

x = Solution().findDisappearedNumbers([2,2])
print(x)