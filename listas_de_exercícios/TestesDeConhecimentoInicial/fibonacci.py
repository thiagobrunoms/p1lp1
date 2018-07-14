#fibonacci

a = 0
b = 1
n = 7
cont = 1
while (cont <= 7):
    soma = a + b 
    print(soma)
    b = a
    a = soma
    
    cont = cont + 1