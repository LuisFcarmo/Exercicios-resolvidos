from typing import List
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        qtd = 0
        for w in words:
            if w.startswith(pref):
                qtd+=1
        return qtd
print(Solution().prefixCount(["leetcode","win","loops","success"], "code"))