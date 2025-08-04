def registro_numeros():
    int1 = int(input("Ingresa tu primer valor: "))
    int2 = int(input("Ingresa tu segundo valor: "))
    int3 = int(input("Ingresa tu tercer valor: "))
    return int1, int2, int3


def devolver_distintos(registro):
    total = 0
    num_mayor = 0 
    num_menor = 0
    list = []
    new_list = []
    
    for numero in registro:
        list.append(numero)
        list.sort()
        total += numero
    
    if total > 15: 
        num_mayor = max(list)
        print(f"La suma de tus numeros fue mayor a 15, esta fue la suma de tus numeros: {total}\nY tu numero mayor es: {num_mayor}")
        return num_mayor
    
    elif total < 10:
        num_menor = min(list)
        print(f"La suma de tus numeros fue menor a 10, esta fue la suma de tus numeros: {total}\nY tu numero menor es: {num_menor}")
        return num_menor
    
    else:
        num_mayor = max(list)
        num_menor = min(list)
        for num in list:
            if num != num_mayor and num != num_menor:
                new_list.append(num)
        print(f"La suma de tus numeros esta en el rango de 10 a 15, esta fue la suma de tus numeros: {total}\nY tu numero intermedio es: {new_list}")
        return new_list



registro = registro_numeros()
devolver_distintos(registro)

