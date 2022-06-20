class A():
    def __init__(self):
        self._contador = contador = 0   #Atributos
        self._cuenta = cuenta = 0   #Atributos   
    
    
    def contador(self): #Metodo
        return self._contador

###########################
#Metodo get
    @property
    def cuenta(self):
        return self._cuenta
###########################


a = A()
print(a.contador()) #se manda a llamar al metodo(Por esos los parentesis)
print(a.cuenta) #Se manda a llamar al metodo, pero al agregra el @property no se usaran los parentesis

'''print(a._contador)  #Incorrecto!
a._contador = 20    #Incorrecto!
print(a._contador)  #Incorrecto!'''

