
def lista_atributos(**kwargs):
    lista = []
    for arg in kwargs.values():
        lista.append(arg)
    print(lista)    
    return lista
lista_atributos(x=1,c=2,d=3,e=4)