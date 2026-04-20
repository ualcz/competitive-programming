a,b=map(int,input().split())

if a>=b:
    print(f'O JOGO DUROU {(24-a)+b} HORA(S)')
else:
    print(f'O JOGO DUROU {(24-a)-(24-b)} HORA(S)')