salario=float(input())

tabela_salario={
    0: 0.15, 
    400.00: 0.12,
    800.00: 0.10,
    1200.00: 0.07,
    2000.00: 0.04
    }
for chave in tabela_salario:
    if salario > chave:
        percentual = tabela_salario[chave]



print(f"Novo salario: {salario*(1+percentual):.2f}")
print(f"Reajuste ganho: {salario*percentual:.2f}")
print(f"Em percentual: {percentual*100:.0f} %")