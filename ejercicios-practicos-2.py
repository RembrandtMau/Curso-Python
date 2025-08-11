def solicitud():
    palabra = (input("Ingresa una palabra: ").lower())
    return palabra

def ordenamiento(palabra):
    unico = []
    for l in palabra:
        if l not in unico:
            unico.append(l) 
    unico.sort()

    print(unico)
    return unico


palabra = solicitud()
ordenamiento(palabra)