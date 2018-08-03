p1 = "motociclista"
p2 = "123456789012"

tam_p1 = len(p1)
tam_p2 = len(p2)

vogais = ["a", "e", "i", "o", "u"]

palavra_cript = ""
if tam_p1 == tam_p2: #deve-se checar ainda se são lower cases.

    for  i, vp1 in enumerate(p1):
        if vp1 == p2[i] and vp1 not in vogais:
            palavra_cript = palavra_cript +p1[i]
        elif i % 2 == 0:
            palavra_cript = palavra_cript + vp1.upper()
        else:
            palavra_cript = palavra_cript + "!!"

else:
    print("As palavras devem ter tamanhos diferentes!")


print (palavra_cript)