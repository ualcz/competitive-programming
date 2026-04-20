casos=int(input())
for i in range(casos):
    resultado=""
    a,b=input().split()
    menor=min(len(a),len(b))
    for j in range(menor):
        resultado+=a[j]+b[j]
    print(resultado+a[menor:]+b[menor:])