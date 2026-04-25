while True:
    x=int(input())
    if x==0:
        break
    s=0
    for i in range(x,x+10):
        if i%2==0:
            s+=i
    print(s)