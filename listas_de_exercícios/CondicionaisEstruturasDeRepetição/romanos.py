romanos = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

valor = "CDLVI"

total = 0
for i in range(1, len(valor)):
    if romanos.get(valor[i]) <= romanos.get(valor[i-1]):
        total = total + (romanos.get(valor[i]) + romanos.get(valor[i-1]))
    else:
        total = total + (romanos.get(valor[i]) - romanos.get(valor[i-1]))

print(total)