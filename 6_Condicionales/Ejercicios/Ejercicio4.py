Candidato = input("Eliga un candidato (A, B o C): ")


if Candidato.upper() == "A":
    print("Usted a votado por el partido rojo")
elif Candidato.upper() == "B":
    print("Usted a votado por el partido verde")
elif Candidato.upper() == "C":
    print("Usted a votado por el partido azul")
else:
    print("Elecion erronea")

