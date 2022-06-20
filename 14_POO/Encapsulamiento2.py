#Antes se utilizaba doble guion bajo para encapsular, actualmente ya no se hcae y ahora solo se coloca un guion bajo
#Python te permitira modificar el valor, sin embargo no es una practica correcta
class A ():
    def __init__(self):
        self._contador = contador = 0 #Encapsulamiento
        self._cuenta = cuenta = 0
    

    def incrementar (self):
        self._contador += 1

    def cuenta (self):
        return self._contador

a = A()
print(a._cuenta)
a._cuenta= 20
print(a._cuenta)