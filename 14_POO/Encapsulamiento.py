class A():
    def __init__(self):
        self.contador = 0
    def incrementar (self):
        self.contador += 1
    def cuenta(self):
        return self.contador

class B():
    def __init__(self):
        self.__contador = 0     #ENCAPSULAMIENTO=>No se puede utilizar los metodos fuera de las funciones
    def incrementar (self):
        self.__contador += 1    #ENCAPSULAMIENTO
    def cuenta(self):
        return self.__contador  #ENCAPSULAMIENTO

a = A()
a.incrementar()
a.incrementar()
print(a.cuenta())
print(a.contador)

b= B()

b.incrementar()
b.incrementar()
print(b.cuenta())
print(b._B__contador)#De esta manera se puede usar los metodos fuera de las funciones