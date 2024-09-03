from itertools import permutations
class Solution:
    def minimumSum(self, num: int) -> int:
        vetnums = [c for c in str(num)]
        vetnums = list(map(lambda x: int(x), vetnums))
        sums = [
            vetnums[0]+vetnums[1],
            
            ]
x = Solution().minimumSum("2932")