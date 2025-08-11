from random import choice
palabras = ['Spiderman', 'PTech', 'Consulting', 'HTB', 'CTF']

def ops(palabras):
    opciones = choice(palabras)
    return opciones

def pista(opciones):

    if opciones == 'Spiderman':
        return("El mejor super héroe del fkn world.")
    
    elif opciones == 'PTech':
        return('Gracias a este equipo IBM sigue de pie.')
    
    elif opciones == 'Consulting':
        return('La mejor área de IBM')
    
    elif opciones == 'HTB':
        return('La mejor página para aprender Hacking')
    
    else:
        return('Los mejores juegos de Hacking')

def juego(opciones, pistas):

    inicio = input("""Bienvenido al mejor juego de fkn mundo. 
El juego es un ahorcado común y corriente, te dare 1 pista y tendras 2 intentos para descubrirlo!!!
Crees ser capaz de lograrlo???? (YES OR NO)\n""").lower()
    
    while inicio not in ("yes", "no"):
        inicio = input("Respuesta invalida, intente otra vez. (YES OR NO)\n").lower()

    if inicio == "yes":    
        palabra = len(opciones)
        palabra_oculta = palabra * '_'
        print(f"""{pistas}
{"  ".join(palabra_oculta)}""")
    else:
        print("Vete a otro lado mi todo tibio...")
    return palabra_oculta

def intentos(opciones, palabra_oculta):

    intentos = 2
    lista_palabra_oculta = list(palabra_oculta)

    while intentos > 0:
        while True:
            letras = input("Adivina adivinador... Qué letra crees que este en la palabra: ").lower().strip()
            
            if len(letras) == 1 and letras.isalpha():
                break
            else:
                print("Solo puedes ingresar un carácter que sea una letra.")

        lista_palabra_oculta = list(palabra_oculta)
        posiciones = []

        posiciones = [i for i, letra in enumerate(opciones.lower()) if letra == letras]

                
        if posiciones:
            for pos in posiciones:
                lista_palabra_oculta[pos] = letras

        else:
            intentos -= 1
            print(f"Letra incorrecta. Te quedan {intentos} intentos.")

        up_palabra_oculta = "".join(lista_palabra_oculta)
        palabra_oculta = up_palabra_oculta  

        print(" ".join(up_palabra_oculta))
        
        if "_" not in up_palabra_oculta:
            print("¡Felicidades, ganaste!")
            break

    if intentos == 0:
        print(f"Mas malo que el cancer. Intentos = {intentos}")


        







opciones = ops(palabras)
pistas = pista(opciones)
palabra_oculta = juego(opciones, pistas)
intentos(opciones, palabra_oculta)
