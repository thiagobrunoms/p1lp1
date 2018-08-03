peso_maximo = 500

#lendo os pesos enquanto o peso lido for diferente de zero
pesos_lidos = []
indice_peso = 1
novo_peso = -1

while (novo_peso != 0):
    novo_peso = int(input("Leia um peso " + str(indice_peso) + ": "))
    pesos_lidos.append(novo_peso)
    indice_peso = indice_peso + 1

soma_pesos = 0
proximo_peso = 0
peso_lido = 0

print(pesos_lidos)

while (soma_pesos <= 500):
    peso_lido = pesos_lidos[proximo_peso]
    print(peso_lido)
    soma_pesos = soma_pesos + peso_lido
    proximo_peso = proximo_peso + 1

if soma_pesos > 500:
    soma_pesos = soma_pesos - peso_lido

print("Peso maximo: " + str(soma_pesos))
print("Quantidade máxima de pessoas: " + str(proximo_peso - 1))




