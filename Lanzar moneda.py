from random import choice
def lanzar_monedas():
    return choice(["Cara", "Cruz"])


def probar_suerte(moneda, lista_numeros):
    if moneda == "Cara":
        lista_numeros.clear()
        print(f"Usted ha obtenido {moneda}. La lista se autodestruira. Lista: {lista_numeros}")
        return("La lista se autodestruirá", lista_numeros)
    else:
        print(f"Uste ha obtenido {moneda}. La lista fue salvada. Su lista es {lista_numeros}")
        return("La lista fue salvada", lista_numeros)


moneda = lanzar_monedas()
lista_numeros = [1, 2, 3, 4, 5]
lanzar_monedas()
probar_suerte(moneda, lista_numeros)