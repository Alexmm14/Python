def Factorial ():
    '''facto=1'''
    from math import factorial
    Num=int(input("Digite el numero para realizar su factorial: "))
    if Num > 0:
        print(factorial(Num))
        '''for i in range(1, Num+1):
            facto= facto*i
        print(facto)'''
    else:
        print("No se puede realizar el factorial de un numero negativo...")
    

Factorial()
