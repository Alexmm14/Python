'''def retorno ():
    <Senetncias>
    return'''

def entero():
    print("Esto es un valor entero...")
    return 10

def decimal():
    print("Esto es un valor Decimal...")
    return 10.5

def frase():
    return "Hola cara de bola..."

'''entero()    #Imprime solo las sentencias de la funcion'''
print(entero()) #imprime el return con las sentencias
print(decimal())
print(frase())

def asignacion ():
    return 1,2,3,4

a,b,c,d = asignacion()

print("{}\n{}\n{}\n{}".format(a,b,c,d))
