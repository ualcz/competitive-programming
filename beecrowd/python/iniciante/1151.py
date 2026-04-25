n=int(input())
lista=[]
for i in range(n):
    if i<=1:
        lista.append(i)
    else:
        lista.append(lista[i-1]+lista[i-2])
print(" ".join(map(str, lista)))