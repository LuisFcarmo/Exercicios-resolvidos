class Solution:
    def interpret(self, command: str) -> str:
        st = ""
        for c in range(len(command)):
            if(command[c] == "(" and command[c+1] == ")"):  
                st +=  "o"
                c += 1
            elif(command[c] != "(" and command[c] != ")"):
                st += command[c]
        return st
print(Solution().interpret("(al)G(al)()()G"))