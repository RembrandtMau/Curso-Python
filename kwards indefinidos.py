def cantidad_atributos(**kwargs):
    parametros = len(kwargs)
    print(parametros)
    return parametros
    

cantidad_atributos(x=1,c=2,e=3,t=4)

def cantidad_atributos(**kwargs):
    parametros = len(kwargs)
    print(parametros)
    return parametros
    
kwargs = {'a': 1,'b':2,'c':3,'d':4}
cantidad_atributos(**kwargs)