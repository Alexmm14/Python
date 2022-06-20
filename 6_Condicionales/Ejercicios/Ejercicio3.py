cadena1= input("Digite una palabra: ")
cadena2= input("Digite otra palbra: ")



if len(cadena1) < 3 or len(cadena2) < 3:
    print("Caracteres insufucientes")    
elif cadena1[-3: ] == cadena2[-3: ]:
    print("Las palabras riman")
elif cadena1[-2: ] == cadena2[-2: ]:
    print("Riman un poco")
else:
    print("Las palbras no riman")

