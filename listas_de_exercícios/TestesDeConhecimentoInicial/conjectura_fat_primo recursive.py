# função recursiva responsável por somar todos os divisores
# primos de um número.
def soma_recursiva(numero):
    """
    Função recursiva responsável por somar todos os divisores
    primos de um número.

    Examples
    --------
    >>> soma_primos = soma_recursiva(20)
         soma_recursiva(20) = return 2 + soma_recursiva(20/2)
    >>> soma_primos = 2 + soma_recursiva(10)
        soma_recursiva(10) = return 2 + soma_recursiva(10/2)
    >>> soma_primos = 2 + 2 + soma_recursiva(5)
        soma_recursiva(5) = 2 + 2 + return 5
    >>> soma_primos = 2 + 2 + 5 = 9

    """

    raiz_numero = int(numero ** 0.5)

    cont = 0
    # percorre de 2 ate a raiz do numero verificando os se existe
    #  algum divisor do numero.
    for cont in range(2, raiz_numero):
        if (numero % cont == 0):
            # se existir algum divisor a função vai rotornar ele somado
            # com a soma dos divisores do novo numero, que é o numero dividido
            # por seu divisor.

            return cont + soma_recursiva(int(numero / cont))

    # caso não seja encontrado nenhum divisor o numero é primo
    # e a soma dos seus divisores é o proprio primo.
    return numero


for number in range(2, 60):
    print(soma_recursiva(number))