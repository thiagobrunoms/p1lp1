quantidade = 0
soma_pesos = 0
novo_peso = -1

while (novo_peso != 0 and quantidade < 7 and soma_pesos <= 560):
    quantidade = quantidade + 1
    novo_peso = int(input("Novo peso: "))
    soma_pesos = soma_pesos + novo_peso

if soma_pesos > 560:
    soma_pesos = soma_pesos - novo_peso
    quantidade = quantidade - 1

print("Peso total: " + str(soma_pesos))
print("Quantidade total de pessoas: " + str(quantidade))


