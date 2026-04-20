def simplificar(num,den):
    if num==0:
        return 0,1
    else:
        a=num
        b=den
        while b!=0:
            r=a%b
            a=b
            b=r
        num=num//a
        den=den//a
        return num,den


n=int(input())
for i in range(n): 
    n1,op1,d1,sin,n2,op2,d2=map(str,input().split())
    n1,n2,d1,d2=int(n1),int(n2),int(d1),int(d2)

    if sin=='+':
        print(f'{(n1*d2 + n2*d1)} / {(d1*d2)} = {simplificar((n1*d2 + n2*d1),(d1*d2))[0]} / {simplificar((n1*d2 + n2*d1),(d1*d2))[1]}')

    elif sin=='-':
        print(f'{(n1*d2 - n2*d1)} / {(d1*d2)} = {simplificar((n1*d2 - n2*d1),(d1*d2))[0]} / {simplificar((n1*d2 - n2*d1),(d1*d2))[1]}')
    elif sin=='*':
        print(f'{(n1*n2)} / {(d1*d2)} = {simplificar((n1*n2),(d1*d2))[0]} / {simplificar((n1*n2),(d1*d2))[1]}')
    elif sin=='/':
        print(f'{(n1*d2) / (n2*d1)} / {(d1*d2)} = {simplificar((n1*d2) // (n2*d1),(d1*d2))[0]} / {simplificar((n1*d2) // (n2*d1),(d1*d2))[1]}')
    