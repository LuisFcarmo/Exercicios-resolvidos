class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        qtd = 0
        while True:
            if(num1 == 0 and num2 == 0):
                return 0
            if(num1 == num2):
                qtd+=1
                break
            if(num1 < num2):
                num2 = num2 - num1
                qtd +=1
            elif(num1 > num2):
                num1 = num1 - num2
                qtd +=1
        return qtd
print(Solution().countOperations(1, 3))
