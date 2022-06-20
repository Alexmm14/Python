def suma():
    global num1, num2 #Si no se usa global, no se puede usar las variables definidas en la funcion fuera de esta
    num1=10
    num2=30
    suma=num1+num2
    return suma

print(suma())

resta = num1 - num2
print(resta)


