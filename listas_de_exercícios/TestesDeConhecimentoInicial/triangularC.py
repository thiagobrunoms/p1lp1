import math
n = 2730

r = int(math.pow(n, 1/3))

if r * (r+1) * (r+2) == n:
    print("Triangular: " + str(r), r+1, r+2)
else:
    print("Nao é Triangular")
