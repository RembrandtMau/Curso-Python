def registro_numeros():
    numeros = []
    for i in range(1, 4):
        numero = int(input(f"Ingresa tu valor {i}: "))
        numeros.append(numero)
        numeros.sort()
    return numeros

def devolver_distintos(registro):
    total = sum(registro)
    num_mayor = max(registro)
    num_menor = min(registro)

    if total > 15: 
        print(f"La suma de tus numeros fue mayor a 15, esta fue la suma de tus numeros: {total}\nY tu numero mayor es: {num_mayor}")
        return num_mayor
    
    elif total < 10:
        print(f"La suma de tus numeros fue menor a 10, esta fue la suma de tus numeros: {total}\nY tu numero menor es: {num_menor}")
        return num_menor
    
    else:
        medio = [n for n in registro if n != num_mayor and n != num_menor]
        print(f"La suma de tus numeros esta en el rango de 10 a 15, esta fue la suma de tus numeros: {total}\nY tu numero intermedio es: {medio}")
        return medio



registro = registro_numeros()
devolver_distintos(registro)

