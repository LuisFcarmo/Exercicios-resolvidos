from itertools import combinations_with_replacement

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        vet = [n for n in range(1, n+1)]
        l = 0
        cn = combinations_with_replacement(vet, 3)
        print(vet)
        for c in cn:
            print(c[0] + c[1] + c[2])
            print(c)
            if((c[0] + c[1] + c[2]) == n):
                if((c[0] <= limit and c[1] <= limit and c[2] <= limit)):
                    l+=1
                
                
        return l
print(Solution().distributeCandies(5, 2))