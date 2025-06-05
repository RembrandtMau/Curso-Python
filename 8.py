

def calculadora (x, y, z):
    if x == float and y == float and z == 1:
        (x + y)
        r = x+y
        print("Tu resultado es: \n %d" % r)
    else:
        print("Valores ingresados no validos.")


def resta(x, y, z):
    if x == float and y == float and z == 2:
        (x - y)
        r = x-y
        print("Tu resultado es: \n %d" % r)
    else:
        print("Valores ingresados no validos.")
    
    

def multiplicacion(x, y, z):
    if x == float and y == float and z == 3:
        (x * y)
        r = x*y
        print("Tu resultado es: \n %d" % r)
    else:
        print("Valores ingresados no validos.")
    

def potencia(x, y, z):
    if x == float and y == float and z == 4:
        (x ** y)
        r = x**y
        print("Tu resultado es: \n %d" % r)
    else:
        print("Valores ingresados no validos.")
    

def division(x, y, z):
    if x == float and y == float and z == 5:
        (x / y)
        r = x/y
        print("Tu resultado es: \n %d" % r)
    else:
        print("Valores ingresados no validos.")
    

def division_sin_residuo(x, y, z):
    if x == float and y == float and z == 6:
        (x // y)
        r = x//y
        print("Tu resultado es: \n %d" % r)
    else:
        print("Valores ingresados no validos.")
    

def modulos(x, y, z):
    if x == float and y == float and z == 7:
        (x % y)
        r = x%y
        print("Tu resultado es: \n %d" % r)
    else:
        print("Valores ingresados no validos.")
    

def main():
    zz = ["Suma: 1", "Resta: 2", "Multiplicación: 3", "Potencia: 4", "División: 5", "División sin residuo: 6", "Residuo sin división: 7"]
    x = input("Ingresa el primer digito que se calculara:\n")
    y = input("Ingresa el segundo digito que se calculara:\n")
    print (zz)
    z = input("Ingresa el tipo de operacion a realizar: \n")
    calculadora()
    resta()
    multiplicacion()
    potencia()
    division()
    division_sin_residuo()
    modulos()