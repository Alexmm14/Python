'''while True:
    try:
        edad=int(input("Ingresa tu edad: "))
        print("Tu edad es de: ", edad)
        break
    except ValueError:
        print("ERROR...")'''

'''while True:
    try:
        num=int(input("Ingresa un numero: "))
        resultado=100/num
        print(resultado)
        break
    except ZeroDivisionError:
        print("ERROR...")
        '''
while True:
    try:
        num=int(input("Ingresa un numero: "))
        resultado=100/num
        print(resultado)
        break
    except KeyboardInterrupt:
        print("Ejecucion interrumpida...")
        break