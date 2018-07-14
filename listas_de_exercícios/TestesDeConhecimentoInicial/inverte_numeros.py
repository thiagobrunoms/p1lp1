number = input("Numero: ")
n_digits = len(number)
number = int(number)
power = n_digits - 1
new_power = 0
inverted_number = 0

while (power >- 1):
    div = 10 ** power
    temp = int(number / div)
    inverted_number = inverted_number + temp * (10 ** new_power)
    number = number % div
    power = power - 1
    new_power = new_power + 1

print(len(str(inverted_number)) )
print(n_digits)
if (len(str(inverted_number)) < n_digits):    
    inverted_number = str(inverted_number)
    n_digits = str(n_digits)
    for zero in range(len(n_digits - len(inverted_number))):
        inverted_number = inverted_number + "0"
        
print("Numero invertido: " + str(inverted_number))
