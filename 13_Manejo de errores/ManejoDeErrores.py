while True:
    try:
        edad= int(input("Ingresa tu edad: "))
        print("Tu edad es: ", edad)
        break
    except:
        print("ERROR...")
    finally:
        print("La ejecucuión a finalizado")