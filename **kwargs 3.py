def describir_persona(nombre, **kwargs):
    for arg in kwargs:
        nombre_argumento = kwargs.keys()
        valor_argumento = kwargs.values()
    print(f"Características de {nombre}:\n{kwargs}")
describir_persona("María", color_ojos="azules", color_pelo="rubio")

def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for nombre_argumento, valor_argumento in kwargs.items():
        print(f"{nombre_argumento}:{valor_argumento}")
describir_persona("María", color_ojos="azules", color_pelo="rubio")
