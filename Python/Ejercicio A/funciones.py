import csv
from csv import DictWriter

def info_clases(desde_archivo):
    datos = {}
    with open(desde_archivo, mode='r', newline='', encoding='utf-8') as archivo:
        lector_csv = csv.DictReader(archivo)
        for fila in lector_csv:
            fila['Clase_id'] = int(fila['Clase_id'])
            datos[fila['Clase_id']] = str(fila['Clase_tipo'])
    return datos

def info_zoo(desde_archivo):
    datos = {}
    with open(desde_archivo, mode='r', newline='', encoding='utf-8') as archivo:
        lector_csv = csv.DictReader(archivo)
        for fila in lector_csv:
            datos[fila['nombre_animal']] = fila
    return datos

def guardar_datos(datos, en_archivo):
    campos = datos.keys()
    list_campos = list(campos)
    with open(en_archivo, 'a') as f_object:
        dictwriter_object = DictWriter(f_object, fieldnames=list_campos)
        dictwriter_object.writerow(datos)
        f_object.close()

def listaclases(datos, clase):
    resultado = []
    for animal in datos.values():
        if int(animal['clase']) == clase:
            resultado.append(animal)
    return resultado

def info_caracteristicas(datos, caracteristica):
    resultado = []
    for animal in datos.values():
        if int(animal[caracteristica]) == 1:
            resultado.append(animal)
    return resultado
