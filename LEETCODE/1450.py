class Solution:
    def busyStudent(self, startTime: list[int], endTime: list[int], queryTime: int) -> int:
        qtd = 0
        for c in range(len(startTime)):
            if(startTime[c] >= queryTime and endTime <= queryTime):
                qtd+=1