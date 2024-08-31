class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr = []
        aux = []
        for num in nums:
            aux.append(num)
            arr.append(sum(aux))
        return arr