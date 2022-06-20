#Metodos = ACCIONES

class FabricaTelefonos():
        #ATRIBUTOS
    marca = "Samsung"
    color = "Azul"
    ram = 32
    almacenamiento = 128

    #METODO DE INSTANCIA
    def llamar(self, mensaje):
        return mensaje
    def escucharMusica (self):
        print("Estas escuchando Música")

telefono = FabricaTelefonos()
#ASIGNACION DE ATRIBUTOS AL OBJET0
telefono.marca
telefono.color
telefono.ram
telefono.almacenamiento

'''print(telefono.marca)
    print(telefono.color)
    print(telefono.ram)
    print(telefono.almacenamiento)'''

print(telefono.llamar("Si bueno, la Z por cual votas?"))
telefono.escucharMusica()