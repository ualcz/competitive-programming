a,b,c=map(float,input().split())

delta1 = b**2 - 4*a*c
if delta1 < 0 or a == 0:
    print('Impossivel calcular')
else:
    R1 = (-b + delta1**(1/2)) / (2*a)
    R2 = (-b - delta1**(1/2)) / (2*a)
    print(f'R1 = {R1:.5f}')
    print(f'R2 = {R2:.5f}')