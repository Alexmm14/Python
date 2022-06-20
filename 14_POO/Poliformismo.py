
from typing import ClassVar


class Animales():
    def __init__(self, nombre, mensaje):
        self.nombre = nombre
        self.mensaje= mensaje
    
    def hablar (self):
        print(self.mensaje)

class Perro(Animales):
    def hablar(self):
        print("Ao mamis") #Se le pueder modificar los metodos de la herencia

class Pez(Animales):
    def hablar(self):
        print("Yo no habalo")

perro = Perro("Firulai", "HOLA PERRAS...")
perro.hablar() #Se manda a llamar al metodo

animales = [Perro("Firulai", "HOLA PERRAS..."), Pez("Nemo", "GLU GLU Glu")]
for i in animales:
    print(i.hablar())

'''pez = Pez("Nemo", "GLU GLU Glu")
pez.hablar()'''

#Polimorfismo, cambiar metodos que vienen de un padre en un hijo