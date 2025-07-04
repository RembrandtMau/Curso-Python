texto = input("Ingresa tu texto:\n").lower()
palabra1 = input("Ingresa una letra que se buscara en tu texto ingresado:\n").lower()
palabra2 = input("Ingresa una letra que se buscara en tu texto ingresado:\n").lower()
palabra3 = input("Ingresa una letra que se buscara en tu texto ingresado:\n").lower()
count1 = texto.count(palabra1)
count2 = texto.count(palabra2)
count3 = texto.count(palabra3)
palabras = len(texto.split())
cantidad = len(texto)
primer_caracter = texto[0]
ultimo_caracter = texto[-1]
inverso = texto[::-1]
aparece_python = "python" in texto
print(f"""
Texto ingresado: {texto}

La primera letra buscada ('{palabra1}') se repite: {count1} veces.
La segunda letra buscada ('{palabra2}') se repite: {count2} veces.
La tercera letra buscada ('{palabra3}') se repite: {count3} veces.
El primer caracter de tu texto es '{primer_caracter}' y el ultimo caracter es '{ultimo_caracter}'.
Tu texto inverso se ve '{inverso}'.
La palabra PYTHON aparece en el texto?? 
respuesta: {aparece_python}
Tu texto tiene {palabras} palabras y {cantidad} caracteres.
""")