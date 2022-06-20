a= int(input("Ingresa el valor A: "))
b= int(input("Ingresa lel valor de B: "))
c= int(input("Ingresa el valor de C: "))

from math import sqrt
z=0
y=0


z= (-b+sqrt((b**2)-(4*a*c)))/(2*a)
y= (-b-sqrt((b**2)-(4*a*c)))/(2*a)


if ((b**2)-(4*a*c)) < 0:
    print("No se puede realizar raiz de un negativo:(")
else:
    print("EL valor de x1 es: ", z)
    print("EL valor de x2 es: ", y)