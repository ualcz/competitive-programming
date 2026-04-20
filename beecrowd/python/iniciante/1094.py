n=int(input())
cobaias=0
coelhos=0
ratos=0
sapos=0
for i in range(n):
    cont,tipo=map(str,input().split())
    if tipo=="C":
        coelhos+=int(cont)
    elif tipo=="R":
        ratos+=int(cont)
    elif tipo=="S":
        sapos+=int(cont)
    cobaias+=int(cont)
print(f"Total: {cobaias} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {coelhos/cobaias*100:.2f} %")
print(f"Percentual de ratos: {ratos/cobaias*100:.2f} %")
print(f"Percentual de sapos: {sapos/cobaias*100:.2f} %")