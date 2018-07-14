n = 2730

i = 0
j = 0
k = 0

while (i * j * k < n):
    i = i + 1
    j = i + 1
    k = j + 1

if i * j * k == n:
    print("TRIANGULAR: " + str(i), str(j), str(k))
else:
    print("NÃO É TRIANGULAR")