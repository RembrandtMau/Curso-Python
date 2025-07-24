lista_numeros = [-1,-2,-3,-4,-5,1,2,3,4,5,1,2,3,4,5]
def todos_positivos(lista_numeros):
    for i in lista_numeros:
        if i >= 0:
            print(i,"true")
            pass
        else:
            print(i,"false")
            


todos_positivos(lista_numeros)
