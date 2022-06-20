class FabricaTelefonos():
    def __init__(self, marca, *colores, **modelo):    #Cuando colocas un * antes del nombre se convierte en una tupla, Si colocas ** se convierte en diccionario
        self.marca = marca
        self.colores = colores
        self.modelo = modelo


telefono = FabricaTelefonos("Samsung", "Azul", "Amarrillo", "Rojo", A=1200, B=1234, C= 1254)
print(telefono.marca)
print(telefono.colores)
print(telefono.modelo)
telefono.memoria = 512#Atributos temporales
print(telefono.memoria )