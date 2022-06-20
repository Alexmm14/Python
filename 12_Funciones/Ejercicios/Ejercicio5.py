def areaCuadrado(base , altura):
    if base == altura:
        cuadradoarea= base*altura
        return cuadradoarea
    else:
        print("No es un cuadrado...")
        return "Error..."
    

def areaCirculo (Radio):
    circuloArea = 3.14*(Radio*Radio)
    return circuloArea


base=float(input("Diguie la base del cuadrado: "))
altura = float(input("Digite la altura del cuadrado: "))
print(areaCuadrado(base, altura))

radio= float(input("Digite la medida del radio de su circulo: "))
print(areaCirculo(radio))