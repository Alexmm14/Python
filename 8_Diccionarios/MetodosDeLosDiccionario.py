diccionarios= {"Nombre": "Alejandro", "Apellido paterno": "Molina", "Edad": 19}
diccionarios2= {1:2, 2:3}

print(diccionarios)
'''
diccionarios.pop("Nombre")#para eliminar un elemento del diccionario, tienen que recibir el parametro a borrar
print(diccionarios)
diccionarios.clear()#Elimina todos los elementos del diccionario 
print(diccionarios.get("Nombre"))#Te muestra el valor de la llave
diccionarios.setdefault("Apellido materno", "Medina")#Agregar un nuevo elemento, primero ingresa la clave y despues su valor
diccionarios.update(diccionarios2)#Une diccionarios
'''
diccionarios.copy()#Hace una copia del diccionario
print(diccionarios)

