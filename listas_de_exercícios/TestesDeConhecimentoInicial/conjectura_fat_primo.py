def is_prime(n):
    num_divs = 0
    for cont in range(2, int(n/2)):
        if n % cont == 0:
            num_divs = num_divs + 1
            break
    else:
        return True

    return False

def factors(n):
    facs = {}
    for f in range(2, int(n/2)+1):
        while (n % f == 0):
            n = n / f
            if f in facs:
                facs[f] = facs.get(f) + 1 
            else: 
                facs[f] = 1
    
    if (len(facs.keys()) == 0):
        facs[n] = 1

    return facs

def calculate_s(number):
    the_factors = factors(number)
    
    s = 0
    for each_factor in the_factors.items():
        s = s + each_factor[0] * each_factor[1]

    print("Soma dos Fatores do número " + str(number) + " = " + str(s))
    if (is_prime(number)):
        if (number == s):
            print("===== Conjectura verdadeira! =====")
        else:
            print("=====================================================")
            print("=====================================================")
            print("=====================================================")
            print("===== Conjectura falsa! =====")
            print("Não atendeu à conjectura!")
    

    return s

for number in range(2, 60):
    calculate_s(number)