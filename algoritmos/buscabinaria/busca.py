import math
def buscabinaria(lista, item, baixo, alto):
    if (baixo <= alto):
        meio = math.ceil((baixo + alto) / 2)
        chute = lista[meio]
        
        if (chute == item): return meio
        elif (chute > item):
            alto = meio - 1
            return buscabinaria(lista, item, baixo, alto)
        else:
            baixo = meio + 1
            return buscabinaria(lista, item, baixo, alto)
    else:
        return None


minha_lista = [1, 3, 5, 7, 9]

print( buscabinaria(minha_lista, 9, 0, len(minha_lista)-1) )# => 1 ❾
print(buscabinaria(minha_lista, 0, 0, len(minha_lista)-1) ) # => None ❿