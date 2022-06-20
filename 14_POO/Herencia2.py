class Animales ():
    def __init__(self, nombre):
        self.nombre = nombre

class Perro (Animales):
    def __init__(self, nombre, sonido):
        #No puedes colocar un init en una clase heredara sin colocar
       super().__init__(nombre)#<===
       self.sonido = sonido#Aqui se le agrega otro atributo
    
perro = Perro("Firulais", "Gouuuu")
print(perro.nombre)
print(perro.sonido)