class Animales ():
    def __init__(self, descripcion, especie, habla):
        self.descripcion = descripcion
        self.especie = especie
        self.habla = habla

    def hablar (self):
        print("Yo hago: ", self.habla)
    
    def describir (self):
        print("Soy de la especie: ", self.especie)

class Perro(Animales): #Se le pasa metodos por herencia
    pass

class Abeja (Animales):
    def sonido(self, sonido):   #Se le pueden agregar mas metodos en la clase, sumados a la de la herencia z
        self.sonido= sonido
        print(self.sonido)

perro = Perro("Perro", "Mamifero", "Guau!!")
perro.hablar()
perro.describir()

abeja = Abeja("Abeja", "Insecto", "BRRRR!!")
abeja.sonido("BRRRR!!!!!")
abeja.hablar()
abeja.describir()

