casoa=int(input())
valor=0
for i in range(casoa):

    a,b=map(int,input().split())
    x,y=min(a,b),max(a,b)
    for j in range(x+1,y):
        if j%2 != 0:
            valor+=j
    print(valor)
    valor=0
