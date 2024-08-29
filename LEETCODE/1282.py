
class Solution:
    def groupThePeople(self, groupSizes):
        dicionario = dict()
        aux = []
        rtn = []
        cont = 0
        for n in range(0, len(groupSizes)):
            dicionario.update({n: groupSizes[n]})
        dicionario = dict(sorted(dicionario.items(), key=lambda item: item[1]))
        for item in dicionario:
            aux.append(item)
            cont+=1
            if cont == dicionario[item]:
                cont = 0
                rtn.append(aux)
                aux = []
        return rtn
                


print(Solution().groupThePeople([3,3,3,3,3,1,3]))