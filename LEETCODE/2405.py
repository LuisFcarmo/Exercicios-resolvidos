class Solution:
    def partitionString(self, s: str) -> int:
        total = ""
        vet = []
        resp = 0
        for c in s:
            if (c not in total):
               total+=c
            else:
                vet.append(total)
                total = c
                resp += 1
        vet.append(total)
        return len(vet)
    
Solution().partitionString("abacaba")