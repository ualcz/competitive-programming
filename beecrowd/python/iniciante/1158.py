n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    s=0
    while True:
        if a%2==0:
            a+=1
        else:
            s+=a
            a+=1
            b-=1
            if b==0:
                break
    print(s)