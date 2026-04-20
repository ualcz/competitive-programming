n=int(input())

for i in range(n):
    verificar=0
    x=int(input())
    for j in range(2,x):
        if x%j==0:
            verificar=1
            break
    if verificar==0 :
        print(f"{x} eh primo")
    else:        
        print(f"{x} nao eh primo")