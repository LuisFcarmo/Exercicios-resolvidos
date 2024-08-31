class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ctd = 0
        for stone in stones:
            if(stone in jewels):
                ctd += 1
        return ctd