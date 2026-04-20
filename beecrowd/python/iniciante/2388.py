n=int(input())
x=0
for i in range(n):
    t,v=map(int,input().split())
    x=(t*v)+x
print(x)