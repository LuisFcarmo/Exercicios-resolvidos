class Solution:
    def unique(self, nums, n):
        qtd=0
        for p in range(len(nums)):
            if n == nums[p]:
                qtd+=1
        if(qtd > 1):
            return False
        return True
    
    def sumOfUnique(self, nums: list[int]) -> int:
        total = 0
        for n in nums:
            if(self.unique(nums,n)):
                total+=n
        return total
print(Solution().sumOfUnique([1,2,3,2]))