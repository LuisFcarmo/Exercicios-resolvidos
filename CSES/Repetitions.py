str = input()
VetCount = []
for c in str:
    total = str.count(c)
    VetCount.append(total)
VetCount.sort()
print(VetCount[len(VetCount)-1])