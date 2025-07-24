from random import randint
nombre = input("Ingresa tu nombre... \n")
print(f"""Bienvendido {nombre} empieza el juego...
    El juego consiste en lo siguiente, yo pensare en un numero aleatorio del 1- 100
    y tu tendras 8 intentos para adivinarlo, listo para juegar??? """)
intentos = 8 
numero_secreto = randint(1,100)
estimacion = 0

while intentos > 0:
    estimacion = int(input(f"Adivina el numero tienes {intentos} intentos restantes. \n"))
    intentos -= 1

    if estimacion < 1 or  estimacion > 100:
        print(f"Tu respuesta ({estimacion}) no esta en el rango solicitado 1-100 asi que no cumple con las reglas del juego.\n")

    elif estimacion > numero_secreto:
        print(f"Tu respuesta ({estimacion}) es mayor al numero que estoy pensando. Intenta de nuevo.\n")

    elif estimacion < numero_secreto:
        print(f"Tu respuesta ({estimacion}) es menor al numero que estoy pensando. Intenta de nuevo.\n")

    elif estimacion == numero_secreto:
        print(f"Felicidades {nombre} has acertado el numero que estaba pensando era {numero_secreto}. Lo resolviste en {8 - intentos}")
        break
    else: 
        print("Ingresa una respuesta valida.")
        continue
if estimacion != numero_secreto:
    print(f"Te quedaste sin intentos {nombre}, mejor suerte la proxima. El numero secreto era {numero_secreto}")
