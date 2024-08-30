class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = 0
        num2 = 0
        for c in range(1, n+1):
            if(c % m == 0):
                num1 +=c
                print(c)
            else:
                num2 +=c
        return num2-num1
    