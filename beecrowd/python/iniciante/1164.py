n=int(input())
for i in range(n):
    x=int(input())
    s=0
    for j in range(1,x):
        if x%j==0:
            s+=j
    if s==x:
        print(f"{x} eh perfeito")
    else:
        print(f"{x} nao eh perfeito")