X,Y=map(int,input().split())

ponteiro=1
for i in range(1,Y+1):
    if ponteiro<X:
        print(i,end=" ")
        ponteiro+=1
    else:
        ponteiro=1
        print(i)

