
dados =list(map(int, input().split()))  
A = dados[0]
posicao = 1
while posicao < len(dados) and dados[posicao] <= 0:
    posicao += 1
N = dados[posicao]
soma = 0
for i in range(N):
    soma += (A + i)
        
print(soma)
