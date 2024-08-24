n = int(input())
odd = [str(c) for c in range(1, n+1) if c%2 == 0]
even = [str(c) for c in range(1, n+1) if c%2 != 0]
if (n in range(1, 4)):
    print("NO SOLUTION")
else:
    print(" ".join(odd + even))