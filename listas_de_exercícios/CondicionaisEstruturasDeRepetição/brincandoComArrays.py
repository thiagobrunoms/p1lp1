deslocamento = int(input("Valor do deslocamento: "))

a = [9, 7, 2, 8, 1, 6, 0] #array de exemplo 
tamanho = len(a)
contador = 0
while (contador < tamanho):
    indice = (deslocamento + contador) % tamanho
    print(a[indice])
    contador = contador + 1

