opc1= int(input("Digite su primer rango: "))
opc2= int(input("Digite el final del rango: "))

for j in range(opc1, opc2+1):
    if j % 2 != 0:
        print(j)
