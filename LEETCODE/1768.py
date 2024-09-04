class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        index01 = 0
        index02 = 0
        final = ""
        if(len(word1) >= len(word2)):
            for c in  word1:
                final += c 
                if(index02 <= len(word2)-1):
                    final += word2[index02]
                index02 += 1
        else:
            for c in  word2:
                if(index01 <= len(word1)-1):
                        final += word1[index01]
                final += c 
                index01 += 1
        return final