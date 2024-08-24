n = int(input())
vet = []
mod = 0

for n in range(0, n):
    number = int(input())
    vet.append(number)
    
for n in range(0, n-1):
    if(vet[n] > vet[n+1]):
        mod += vet[n]-vet[n+1]
print(mod)