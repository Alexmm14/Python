diccionario= {

    1 : "Casillas", 15 : "Ramos",

    3 : "Pique", 5 : "Puyol",

    11 : "Capdevila", 14 : "Xabi Alonso",

    16 : "Busquets", 8 : "Xavi Hernandez",

    18 : "Pedrito", 6 : "Iniesta",

    7 : "Villa"

}

busqueda= int(input("Digite el número del jugador: "))

if busqueda in diccionario:
    print(diccionario[busqueda])
else:
    print("jugador no encontrado")
