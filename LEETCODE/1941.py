class Solution:
    def vowelStrings(self, words, left: int, right: int) -> int:
        qtd = 0
        vogais = ['a', 'e', 'i', 'o', 'u']
        for c in range(left, right+1):
            if(str.lower(words[c][0]) in vogais and str.lower(words[c][len(words[c])-1]) in vogais):
               qtd+=1
        return  qtd
Solution().vowelStrings(["hey","aeo","mu","ooo","artro"],1,4)