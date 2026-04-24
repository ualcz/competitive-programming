
def media(n1,n2):
    if n1<0 or n1>10 or n2<0 or n2>10:
            print('nota invalida')
            return True
    else:
        media=(n1+n2)/2
        print(f'media = {media:.2f}')
        print('novo calculo (1-sim 2-nao)')
        op=int(input())
        if op==1:
             return True
        return False

  

ponteiro=0
i=0
isactieve=True
while isactieve:
    x=float(input())
    if ponteiro==0:
        n1=x
        ponteiro=1
        i+=1
    elif ponteiro==1:
        n2=x
        ponteiro=0
        i+=1
    if i>=2:
        isactieve=media(n1,n2)
        i=0
    
    


        
    
