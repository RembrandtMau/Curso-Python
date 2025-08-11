from random import choice
palabras = ['Spiderman', 'P-Tech', 'Consulting', 'HTB', 'CTF']
opciones = choice(palabras)
def pista(palabras):
    for pista in palabras:
        if pista == 'Spiderman':
            spiderman = print("El mejor super héroe del fkn world.")
            return spiderman
        elif pista == 'P-Tech':
            ptech = print('Gracias a este equipo IBM sigue de pie.')
            return ptech
        elif pista == 'Consulting':
            consulting = print('La mejor área de IBM')
            return consulting
        elif pista == 'HTB':
            htb = print('La mejor página para aprender Hacking')
            return htb
        else:
            ctf = print('Los mejores juegos de Hacking')
            return ctf
    

pista(palabras)