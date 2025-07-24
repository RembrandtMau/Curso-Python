from random import randint
def lanzar_dados():
    dado_uno = randint(1,6)
    dado_dos = randint(1,6)
    return[dado_uno, dado_dos]
lanzar_dados()
def evaluar_jugada(dado1, dado2):
    result = dado1 + dado2
    if result <= 6:
        return (f"La suma de tus dados es {result}. Lamentable")
    elif 6 < result < 10:
        return(f"La suma de tus dados es {result}. Tienes buenas chances")
    elif result >= 10:
        return(f"La suma de tus dados es {result}. Parece una jugada ganadora")

dados = lanzar_dados()
evaluar_jugada(dados[0], dados[1])