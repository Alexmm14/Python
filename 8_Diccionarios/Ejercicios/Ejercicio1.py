disccionarioM = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

busqueda=input("Ingresa el pais que deseas buscar: ")
verificar= busqueda.capitalize() in disccionarioM

if verificar == True:
    print(disccionarioM[busqueda.capitalize()])
else:
    print("Pais no encontrado")
