def TowPointers(n, max, vect):
    vect.sort()
    i, k = 0, 0
    total = 0
    k = len(vect)-1
    
    while i <= k:
        if vect[i] + vect[k] <= max:
            total += 1
            i +=1
            k -= 1
        else:
            k -= 1
            total += 1    
    return total
    
n, max = map(int, input().split())
vect = list(map(int, input().split()))
print(TowPointers(n, max,vect))