def reducir_lista(lista_numeros):
    lista = set(lista_numeros)
    lista.remove(max(lista))
    
    return lista

def promedio(lista):
    promedio = 0
    for n in lista:
        promedio += n
    numeros = len(lista)
    promedio = promedio / numeros
    print(promedio)
    return promedio

lista_numeros = [1, 2, 3, 4, 5, 6, 8, 8, 3]
lista = reducir_lista(lista_numeros)
promedio(lista)
reducir_lista(lista_numeros)

