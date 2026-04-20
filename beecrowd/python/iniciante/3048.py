n=int(input())
b=None
x=0
for i in range(n):
    v=int(input())
    if v!=b:
        (b,x)=v,x+1
print(x)