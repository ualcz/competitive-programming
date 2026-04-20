consumo={
    1:300,
    2:1500,
    3:600,
    4:1000,
    5:150
}
x=0
for i in range(1,6):
    n=int(input())
    x=(consumo[i])*n+x
print(x+225)