
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        result = 0
        for op in operations:
            if(op == "X++"):
                result +=1
            elif(op == "++X"):
                result += 1
            elif(op == "X--"):
                result -= 1
            elif(op == "--X"):
                result -=1
        return result