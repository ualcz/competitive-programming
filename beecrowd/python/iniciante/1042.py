a,b,c=map(int,input().split())

print(min(a,b,c))

if a!=max(a,b,c) and a!=min(a,b,c):
    print(a)

elif b!=max(a,b,c) and b!=min(a,b,c):
    print(b)

elif c!=max(a,b,c) and c!=min(a,b,c):
    print(c)

print(max(a,b,c))
print('')
print(a)
print(b)
print(c)