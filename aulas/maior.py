#imprimir em ordem 3 números dados pelo usuário

a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))
c = int(input("Digite o terceiro numero: "))

if a > b:
    if a > c:
        if b > c:
            print(a, b, c)
        else:
            print(a, c, b)
    else:
        print(c, a, b)
else:
    if b > c:
        if a > c:
            print (b, a, c)
        else:
            print (b, c, a)
    else:
        print (c, b, a)
