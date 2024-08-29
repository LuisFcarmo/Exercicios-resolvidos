class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours, target: int) -> int:
        acumulador = 0
        for h in hours:
            if(h >= target):
                acumulador+=1