from typing import List
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        resp = []
        for index in range(0, len(words)):
            print(index)
            if(x in words[index]):
                resp.append(index)
        return resp
print(Solution().findWordsContaining(["leet","code"], "e"))