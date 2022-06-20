def factura ():
    Cantidad = float(input("Digite la cantidad comprada: "))
    iva = float(input('Digite el porcentaje del IVA(En caso de digitar 0, se establecera 21 porciento de IVA): '))
    if iva == 0:
        factura= Cantidad+((Cantidad*21)/100)
        return factura
    elif iva > 0:
        factura= Cantidad+((Cantidad*iva)/100)
        return factura
    else:
        print("IVA NO VALIDO...")
        return "ERROR"
 
print(factura())