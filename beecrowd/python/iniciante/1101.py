
while True:
    soma=0
    m,n=map(int,input().split())
    if m<=0 or n<=0:
        break
    for i in range(min(m,n),max(m,n)+1):
        print(f'{i}',end=' ')
        soma+=i
    print(f'Sum={soma}')