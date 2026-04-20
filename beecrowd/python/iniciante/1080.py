valormaior=0
posicao=0
for i in range(1,101):
    valor=int(input())
    if valor>valormaior:
        valormaior=valor
        posicao=i

print(valormaior)
print(posicao)