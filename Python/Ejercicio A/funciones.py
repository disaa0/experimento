import csv
from csv import DictWriter

def mostrar_datos_clases(desde_archivo):
    datos = {}
    with open(desde_archivo, mode='r', newline='', encoding='utf-8') as archivo:
        lector_csv = csv.DictReader(archivo)
        for fila in lector_csv:
            fila['Clase_id'] = int(fila['Clase_id'])
            datos[fila['Clase_id']] = str(fila['Clase_tipo'])
    return datos

def mostrar_datos_zoo(desde_archivo):
    datos = {}
    with open(desde_archivo, mode='r', newline='', encoding='utf-8') as archivo:
        lector_csv = csv.DictReader(archivo)
        for fila in lector_csv:
            datos[fila['nombre_animal']] = fila
    return datos

def listar_x_clase(datos, clase):
    resultado = []
    for animal in datos.values():
        if int(animal['clase']) == clase:
            resultado.append(animal)
    return resultado

def listar_x_caracteristica(datos, caracteristica):
    resultado = []
    for animal in datos.values():
        if int(animal[caracteristica]) == 1:
            resultado.append(animal)
    return resultado
