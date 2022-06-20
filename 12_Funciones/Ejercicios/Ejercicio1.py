lista =[]

elementosAA= int(input("Digite cuantos elementos desea agregar: "))

def agregarLista():
    
    for i in range(elementosAA):
        elementosA= float(input("Digite el elemento a agregar: "))
        lista.append(elementosA)
    
def ordenarLista():
    lista.sort()
    listapar=[]
    listaimpar=[]
    for i in range(elementosAA):
        if lista[i] % 2 == 0:
            listapar.append(lista[i])
        else:
            listaimpar.append(lista[i])
    
    print(listapar)
    print(listaimpar) 


    
agregarLista()
ordenarLista()