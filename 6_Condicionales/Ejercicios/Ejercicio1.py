vocal = input("Digite una vocal:")
'''
if vocal.lower() == "a":
    print("Esta vocal es la A")
elif vocal.lower()=="e":
    print("Esta vical es la E")
elif vocal.lower() == "i":
    print("Esta vical es la I")
elif vocal.lower() == "o":
    print("Esta vical es la O")
elif vocal.lower() == "u":
    print("Esta vocal es la U")
else:
    print("Esta no es una vocal")'''

if vocal.lower() in "aeiou": #Si esta dentro de aeiou
    print("Es una vocal")
else: print("No es un vocal")

