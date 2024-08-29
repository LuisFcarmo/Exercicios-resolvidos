class Solution:
    def verify(self, num):
        cp1 = num
        cp2 = num
        op = 0
        while(True):
            if(cp1%3 == 0): break
            if (cp2%3 == 0): break
            cp1-=1
            cp2+=1
            op += 1
        return op
    
    def minimumOperations(self, nums):
        total = 0
        for n in nums:
            total += self.verify(n)
        return total
    
x = Solution()
print(x.minimumOperations([1,2,3,4]))
