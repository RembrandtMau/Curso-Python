numero = int(input("Ingresa un numero: "))
inicio = 1

def contar_primos(numero):
    global inicio
    while inicio <= numero:
        x = 0 
        contador = 1
        while contador <= inicio:
            if inicio % contador == 0:
                x = x + 1
            contador += 1
        if x == 2:
            print(inicio)
        inicio += 1

contar_primos(numero)
