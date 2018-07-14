numero = 17

for cada_elemento in range(2, int(numero / 2) + 1):
    if numero % cada_elemento == 0:
        print("Não é primo!")
        break
else: #É executado caso não encontre um break dentro do for
    print("O numero é primo!")

