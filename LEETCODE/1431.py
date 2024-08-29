class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        vet = []
        atual_max = 0
        for c in candies:
            atual_max = max(candies)
            if (c + extraCandies) >= atual_max:
                vet.append(True)
            else:
                vet.append(False)
        return vet

print(Solution().kidsWithCandies([2,3,5,1,3], 3))