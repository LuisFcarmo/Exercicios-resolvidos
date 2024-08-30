from typing import List
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maior = 0
        for row in accounts:
            if(maior < sum(row)):
                maior = sum(row)
        return maior
               
print(Solution().maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))