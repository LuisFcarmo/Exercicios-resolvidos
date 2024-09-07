class Solution:
    def maximumNumberOfStringPairs(self, words:list[str]) -> int:
        qtd = 0
        for index in range(len(words)):
            if words.count(words[index][::-1]) > 0:
                qtd += 1
                print(qtd)
            if(words[index] == words[index][::-1]):
                print(words[index])
                print(words[index][::-1])
                qtd-=1
                
        return qtd 
print(Solution().maximumNumberOfStringPairs(["sa","ue","ss","df","au","ru","id","ur"]))