'''
class FabricaTelefonos():
    marca = "Samsung"

    def ElaborarHuawei(self):
        
        self.marca="Huawei" #Englobar un atributo a toda la clase

telefono = FabricaTelefonos()
telefono.ElaborarHuawei()

print(telefono.marca)        '''

class FabricaTelefonos():
    def __init__(self, marca, color): #Metodo de python
        self.marca = marca
        self.color = color

''' print("Se esta ejecutando el metodo init, porque se ha creado un nuevo objeto")#Se ejeecuta cuando se crea un nuevo objeto'''
        
telefono = FabricaTelefonos("Samsung", "Azul")# Se le pasan como argumentos los atributos
print(telefono.marca)
print(telefono.color)