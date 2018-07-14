import random
array1 = list(range(random.randint(1, 10)))
array2 = list(range(random.randint(1, 10)))

n_a1 = random.randint(1, len(array1))
n_a2 = random.randint(1, len(array2))

print(array1)
print(array2)

print("Quantidade de numeros a serem selecionados: ")
print("Array 1: " + str(n_a1))
print("Array 2: " + str(n_a2))


