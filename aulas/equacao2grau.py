import math

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

delta = (b ** 2) - 4 * a * c

print("O valor de delta é " + str(delta))
if (delta > 0):
    x1 = ( (-1*b) + math.sqrt(delta)) / (2*a)
    x2 = ( (-1*b) - math.sqrt(delta)) / (2*a)
    print("As raízes são " + str(x1) + " e " + str(x2))
elif delta == 0:
    x = ( (-1*b) + math.sqrt(delta)) / (2*a)
    print("A raiz é " + str(x))
else:
    print("Não há raízes reais!")



