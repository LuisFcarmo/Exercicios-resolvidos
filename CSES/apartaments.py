def MaxAprt(n, m, k, candidatos, apartamentos):
    candidatos.sort()
    apartamentos.sort()
    total = 0
    j, i = 0, 0
    while i < n and j < m:
        if apartamentos[j] + k < candidatos[i]:
            j += 1
        elif apartamentos[j] - k > candidatos[i]:
            i += 1
        else:
            total += 1
            i += 1
            j += 1
    return total

n, m, k = map(int, input().split())
candidatos = list(map(int, input().split()))
apartamentos = list(map(int, input().split()))
print(MaxAprt(n, m, k, candidatos, apartamentos))