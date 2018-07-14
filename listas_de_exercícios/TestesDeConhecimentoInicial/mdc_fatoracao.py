#mdc via fatoração

a = 120
b = 35

divisores = []

i = 2
for i in range(2, int(a/2)):
    print (a, b)
    while (a % i == 0 and b % i == 0):
        print ("in " + str(a), b)
        if i not in divisores:
            divisores.append(i)
        
        a = a / i
        b = b / i

    i = i + 1

mdc = 1
for div in divisores:
    mdc = mdc * div

print (mdc)