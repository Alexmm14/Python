class A():
    def __init__(self):
        self._contador = contador = 0   #Atributos
        self._cuenta = cuenta = 0   #Atributos   
    
    
    @property
    def cuenta(self):
        return self._cuenta
    
    @cuenta.setter #Metodo Seet
    def cuenta(self, cuenta):
        self._cuenta = cuenta

    @property
    def contador(self):
        return self._contador
    
    @contador.setter
    def contador(self, contador):
        self._contador = contador


a = A()
'''print(a.contador()) #se manda a llamar al metodo(Por esos los parentesis)'''
print(a.cuenta)
a.cuenta = 30
print(a.cuenta) #Se manda a llamar al metodo, pero al agregra el @property no se usaran los parentesis
print(a.contador)
a.contador = 20
print(a.contador)

'''print(a._contador)  #Incorrecto!
a._contador = 20    #Incorrecto!
print(a._contador)  #Incorrecto!'''
