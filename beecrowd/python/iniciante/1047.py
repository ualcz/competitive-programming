a, b, c, d = map(int, input().split())

inicio_total = a * 60 + b
fim_total = c * 60 + d

duracao_total = fim_total - inicio_total

if duracao_total <= 0:
    duracao_total += 24 * 60

horas = duracao_total // 60
minutos = duracao_total % 60

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")