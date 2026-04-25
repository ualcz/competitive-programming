x=int(input())
total=0
quant=0
while True:
    y=int(input())
    if y>x:
        for i in range(x,y+1):
            total+=i
            quant+=1
            if total>y:
                break
        break
   
print(quant)