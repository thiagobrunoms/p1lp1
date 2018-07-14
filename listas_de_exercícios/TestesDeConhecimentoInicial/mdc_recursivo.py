#mdc recursivo
def euclides(dividendo, divisor):
    if (divisor == 0):
        return dividendo
    else:
        return euclides (divisor, dividendo % divisor)


print(euclides(135, 40))