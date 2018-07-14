#primo
contador = 2
numero = 17
limite = int(numero / 2)
while (contador <= limite ):
    if numero % contador == 0:
        print ("Não é primo!")
        break
    contador = contador + 1

if contador == limite + 1:
    print ("O numero é primo!")
