from typing import List

class Solution:
    def FindWords(self, products, c):
        arr = []
        for p in products:
            if (p.startswith(c)):
                arr.append(p)
        arr = sorted(arr)
        return arr[:3]
    
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        resp = []
        prefix = ""
        products.sort()
        for c in searchWord:
            prefix += c
            resp.append(self.FindWords(products, prefix))
        return resp
Solution().suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], "mouse")
