class Solution:
    def scoreOfString(self, s: str) -> int:
        maximo = []
        aux_vet = []
        for word in s:
            aux_vet = word.split(" ")
            maximo.append(len(aux_vet))
        return max(maximo)
