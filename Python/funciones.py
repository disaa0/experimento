import csv
def leer_csv(nombre_archivo):
    with open(nombre_archivo, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        lista_dict = []
        for row in reader:
            lista_dict.append(row)
        return lista_dict

def list_to_dict(lista, llave):
    diccionario = {}
    for dicc in lista:
        diccionario[dicc[llave]] = dicc
    return diccionario


def filtrar_x_criterio(dicc_animales, criterio, valor):
    lista_animales = []
    for animal, diccionario in dicc_animales.items():
        if diccionario[criterio] == valor:
            lista_animales.append(diccionario)
    return lista_animales

def organizar_x_valor(dicc_animales, criterio):
    dicc_animales_filtrado = {}
    for animal, diccionario in dicc_animales.items():
        if diccionario[criterio] not in dicc_animales_filtrado:
            dicc_animales_filtrado[diccionario[criterio]] = []
            dicc_animales_filtrado[diccionario[criterio]].append(diccionario)
        else:
            dicc_animales_filtrado[diccionario[criterio]].append(diccionario)
    return dicc_animales_filtrado