qtd = int(input())

while(qtd != 0):
    st = str(input())
    ac = 0
    for s in st:
        ac += int(s)
    print(ac)
    qtd -=1
