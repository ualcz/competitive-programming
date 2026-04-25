s = 0
i = 1
for j in range(1,20):
    s += (2*j-1)/i
    i *= 2
print(f"{s:.2f}")