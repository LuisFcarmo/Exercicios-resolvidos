class Solution:
    def removeDuplicates(self, nums) -> int:
        ic = 0
        cont = 0
        for n in nums:
            if(cont == 0):
                ant = n
                cont += 1
            else:
                if(ant != n):
                    nums[ic] = ant
                    ic+=1
                ant = n
            nums[ic] = ant
        return ic
            
x = Solution()
print(x.removeDuplicates([1,1,2]))