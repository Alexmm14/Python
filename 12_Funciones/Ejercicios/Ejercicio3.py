def numeros ():
    num= float(input("Digite su primer numero: "))
    num2= float(input("Digite su segundo numero: "))
    if num > num2:
        return 1
    elif num2 > num:
        return -1
    else:
        return 0
    
print(numeros())