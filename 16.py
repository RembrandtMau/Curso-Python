def cantidad_pares(lista_numeros):
    numero_par = 0
    for numero in lista_numeros:
        if numero % 2 == 0:
            numero_par += 1
    return numero_par
    
    
lista_numeros = [1, 2, 3 , 4, 4, 4, 4,]
resultado = cantidad_pares(lista_numeros)        
print(resultado)