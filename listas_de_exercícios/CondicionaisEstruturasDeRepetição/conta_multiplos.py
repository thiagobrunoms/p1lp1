a = int(input("Numero 1: "))
b = int(input("Numero 2: "))

quantidade_multiplos = 0
for i in range(1, 50):
    if i % a == 0 and i % b == 0:
        quantidade_multiplos = quantidade_multiplos + 1

print("Quantidade de múltiplos entre " + str(a) + " e " + str(b) + " = " + str(quantidade_multiplos))
