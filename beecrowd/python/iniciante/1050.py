a=int(input())

ddd={
    11:'Sao paulo',
    61:'Brasilia',
    71:'Salvador',
    21:'Rio de Janeiro',
    32:'Juiz de Fora',
    19:'Campinas',
    27:'Vitoria',
    31:'Belo Horizonte'
}

if a in ddd:
    print(ddd[a])
    
else:
    print("DDD nao cadastrado")