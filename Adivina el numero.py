from random import *
nombre = input("Ingresa tu nombre... \n")
print(f"""Bienvendido {nombre} empieza el juego...
    El juego consiste en lo siguiente, yo pensare en un numero aleatorio del 1- 100
    y tu tendras 8 intentos para adivinarlo, listo para juegar??? """)
intentos = 8 
respuesta = randint(1,100)
print (respuesta)
while intentos > 0:
    intento = input(f"Adivina el numero tienes {intentos} intentos restantes. \n")
    print (respuesta)
    if int(intento) == respuesta:
        print(f"Felicidades has acertado el numero que estaba pensando era {respuesta}.")
        break
    
    elif int(intento) < 1:
        print(f"Tu respuesta ({intento}) es menor al parametro solicitado 1-100 asi que no cumple con las reglas del juego.\nTe quedan {intentos - 1} intentos.\n")
        intentos = intentos - 1
    elif int(intento) > 100:
        print(f"Tu respuesta ({intento}) es mayor al parametro solicitado 1-100 asi que no cumple con las reglas del juego.\nTe quedan {intentos - 1} intentos.\n")
        intentos = intentos -1

    elif int(intento) > respuesta:
        print(f"Tu respuesta ({intento}) es mayor al numero que estoy pensando. Intenta de nuevo.\nTe quedan {intentos - 1} intentos.\n")
        intentos= intentos - 1

    elif int(intento) < respuesta:
        print(f"Tu respuesta ({intento}) es menor al numero que estoy pensando. Intenta de nuevo.\nTe quedan {intentos - 1} intentos.\n")
        intentos = intentos - 1
    else: 
        print(f"Ingresa una respuesta valida.\nTe quedan {intentos - 1} intentos.\n")
        intentos = intentos - 1


