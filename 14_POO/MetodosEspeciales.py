

class Persona ():
#       Metodo constructor
    def __init__(self, Nombre, edad):
        self.Nombre = Nombre
        self.edad = edad
        print("El sujeto {}, tiene {} años".format(self.Nombre, self.edad))
    
    def __str__(self):
        return "El sujeto tienen como atributo el nombre de {} y edad de {} años".format(self.Nombre, self.edad)
    

#       Metodo Desconstructor
    def __del__(self):
        print("El sujeto {} de {} años, se ha eliminado".format(self.Nombre, self.edad))
    

persona = Persona("Alejandro", 19)
print(str(persona))