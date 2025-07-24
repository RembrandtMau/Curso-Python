def suma_menores(lista_numeros):
    suma = 0
    for numero in lista_numeros:
        if 0 < numero < 1000:
            suma += numero
    return suma

# Ejemplo de uso
lista_numeros = [150, -20, 999, 1000, 45, 0, 1050, 300]
resultado = suma_menores(lista_numeros)
print("La suma de los números mayores a 0 y menores a 1000 es:", resultado)
