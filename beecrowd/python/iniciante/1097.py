i = 0
while i <= 2:
    for j in [1, 2, 3]:
        valor_j = j + i

        if i == 0 or i == 1 or i >= 1.9:
            print(f"I={i:.0f} J={valor_j:.0f}")
        else:
            print(f"I={i:.1f} J={valor_j:.1f}")
            
    i += 0.2