Numero = int(input("Digite un numero: "))


if Numero < 0:
    #Numero= Numero * -1
    print("EL valor absoluto de {}, es: {}".format(Numero, abs(Numero)) )#abs te da el valor absoluto
else:
    print("EL valor absoluto de {} es: {}".format(Numero, Numero))