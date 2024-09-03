class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vogais = ['a', 'e', 'i', 'o', 'u']
        m1 = s[0: int(len(s)/2)]
        m2 = s[int(len(s)/2): len(s)]
        qtd1 = 0
        qtd2 = 0
        for c in m1:
            if str.lower(c) in vogais:
                qtd1 += 1
        for c in m2:
            if str.lower(c) in vogais:
                qtd2 += 1
        if(qtd2==qtd1):
            return True
        return False
print(Solution().halvesAreAlike("book"))