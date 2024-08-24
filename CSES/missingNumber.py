n = int(input())
vet = []

for n in range(0, n):
    number = int(input())
    vet.append(number)

for n in range(0, n-1):
    if (vet[n+1] - vet[n]) != 1:
        print(vet[n]+1)
