#ano bissexto: 
# multiplo de 4 e não for divisível por 100 / ou ser múltiplo de 400

ano = int(input("Digite o ano: ")) #input retorna string

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print("O ano " + str(ano) + " é bissexto!")
else:
    print("O ano " + str(ano) + " não é bissexto!") 
