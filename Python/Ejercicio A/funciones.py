import csv 
def mostrardatos(Archivo):

    datos = {}
    with open(Archivo, mode='r', newline='', encoding='utf-8') as archivo:
         lector_csv = csv.DictReader(archivo)
         for fila in lector_csv:
           fila['Clase_id'] = int(fila['Clase_id'])
           datos[fila['Clase_id']] = str(fila['Clase_tipo'])
    return datos


def mostrardatosanimales(Archivo):
    datos = {}
    with open(Archivo, mode='r', newline='', encoding='utf-8') as archivo:
        lector_csv = csv.DictReader(archivo)
        for fila in lector_csv:
            datos[fila['nombre_animal']] = fila
    return datos

def Clase(Infoanimal,Idanimal):

    resultado = []
    for animal in Infoanimal.values():
        if int(animal['clase']) == Idanimal:
            resultado.append(animal)
    return resultado
def Caracteristica(Infoanimal,Caracteristica):
    resultado = []
    for animal in Infoanimal.values():
        if int(animal[Caracteristica]) == 1:
            resultado.append(animal)
    return resultado

def AgregarAnimal():
    pass
