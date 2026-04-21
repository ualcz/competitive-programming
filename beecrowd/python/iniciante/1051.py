valor=float(input())
imposto=0.00

if valor >= 2000.01 and valor <= 3000.00:
    imposto = (valor - 2000.01) * 0.08

elif valor >= 3000.01 and valor <= 4500.00:

    imposto = (1000.00 * 0.08) + ((valor - 3000.01) * 0.18)

elif valor > 4500.00:

    imposto = (1000.00 * 0.08) + (1500.00 * 0.18) + ((valor - 4500.01) * 0.28)

if imposto == 0.00:
    print("Isento")
else:
    print(f"R$ {imposto:.2f}")